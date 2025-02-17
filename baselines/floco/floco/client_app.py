"""floco: A Flower Baseline."""

import copy

import torch

from floco.dataset import load_dataloaders
from floco.model import Net, SimplexModel, get_weights, set_weights, test, train
from flwr.client import ClientApp, NumPyClient
from flwr.common import Context, ParametersRecord, array_from_numpy, bytes_to_ndarray


class FlowerClient(NumPyClient):
    """A class defining the client."""

    def __init__(
        self,
        partition_id,
        global_model,
        pers_model,
        pers_lamda,
        trainloader,
        valloader,
        local_epochs,
        device,
        context,
    ):
        self.partition_id = partition_id
        self.global_model = global_model
        self.pers_model = pers_model
        self.trainloader = trainloader
        self.valloader = valloader
        self.local_epochs = local_epochs
        self.device = device

        # Floco+ params
        self.pers_lamda = pers_lamda
        if self.pers_lamda != 0:
            self.client_state = context.state
            if "pers_parameters" not in self.client_state.parameters_records:
                self.client_state.parameters_records["pers_parameters"] = (
                    ParametersRecord()
                )

    def fit(self, parameters, config):
        """Train model using this client's data."""
        set_weights(self.global_model, parameters)
        reg_parameters = copy.deepcopy(list(self.global_model.parameters()))
        train_loss = self._train(self.global_model, config)

        if self.pers_lamda != 0:
            param_record = self.client_state.parameters_records["pers_parameters"]
            if len(param_record) > 0:
                self._set_local_weights()
            self._train(self.pers_model, config, reg_parameters, self.pers_lamda)
            self.client_state.parameters_records["pers_parameters"] = (
                self._get_local_weights(self.pers_model)
            )

        return (
            get_weights(self.global_model),
            len(self.trainloader.dataset),
            {"train_loss": train_loss},
        )

    def evaluate(self, parameters, config):
        """Evaluate model using this client's data."""
        set_weights(self.global_model, parameters)
        model = self.global_model
        if self.pers_lamda != 0:
            param_record = self.client_state.parameters_records["pers_parameters"]
            if len(param_record) > 0:
                model = self.pers_model
                self._set_local_weights()
            else:
                model = self.global_model
        self._set_simplex_params(model, config, training=False)
        loss, accuracy = test(model, self.valloader, self.device)
        return loss, len(self.valloader.dataset), {"loss": loss, "accuracy": accuracy}

    def get_properties(self, config):
        """Return the properties of this client."""
        return {"partition-id": self.partition_id}

    def _train(self, model, config, reg_parameters=None, lamda=0):
        """Set simplex parameters and train."""
        self._set_simplex_params(model, config, training=True)
        train_loss = train(
            model,
            self.trainloader,
            self.local_epochs,
            self.device,
            reg_parameters,
            lamda,
        )
        return train_loss

    def _set_simplex_params(self, model, config, training=None):
        """Set simplex parameters, i.e. projected point and sampling radius."""
        model.training = bool(training)
        if all(key in config for key in ["center", "radius"]):
            model.subregion_parameters = (
                bytes_to_ndarray(config["center"]),
                config["radius"],
            )

    def _set_local_weights(self):
        """Set local client model weights."""
        pers_state_dict = {
            k: torch.from_numpy(v.numpy())
            for k, v in self.client_state.parameters_records["pers_parameters"].items()
        }
        self.pers_model.load_state_dict(pers_state_dict)

    def _get_local_weights(self, model):
        """Get local client model weights."""
        p_record = ParametersRecord(
            {
                k: array_from_numpy(v.detach().cpu().numpy())
                for k, v in model.state_dict().items()
            }
        )
        return p_record


def client_fn(context: Context):
    """Construct a Client that will be run in a ClientApp."""
    # Load model and data
    device = torch.device(
        "cuda:0"
        if torch.cuda.is_available()
        else "mps" if torch.backends.mps.is_available() else "cpu"
    )
    seed = int(context.run_config["seed"])
    endpoints = int(context.run_config["endpoints"])
    local_epochs = int(context.run_config["local-epochs"])
    pers_model = None
    pers_lamda = 0

    if context.run_config["algorithm"] == "FedAvg":
        global_model = Net(seed=seed).to(device)
    elif context.run_config["algorithm"] == "Floco":
        global_model = SimplexModel(endpoints=endpoints, seed=seed).to(device)
        pers_lamda = int(context.run_config["pers_lamda"])
        if pers_lamda != 0:
            pers_model = SimplexModel(endpoints=endpoints, seed=seed).to(device)
    else:
        raise ValueError("Algorithm not implemented")

    partition_id = int(context.node_config["partition-id"])
    num_partitions = int(context.node_config["num-partitions"])
    trainloader, valloader, _ = load_dataloaders(partition_id, num_partitions, context)

    # Return Client instance
    return FlowerClient(
        partition_id,
        global_model,
        pers_model,
        pers_lamda,
        trainloader,
        valloader,
        local_epochs,
        device,
        context,
    ).to_client()


# Flower ClientApp
app = ClientApp(client_fn)
