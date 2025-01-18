# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2
from flwr.proto import log_pb2 as flwr_dot_proto_dot_log__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import serverappio_pb2 as flwr_dot_proto_dot_serverappio__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in flwr/proto/serverappio_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ServerAppIoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRun = channel.unary_unary(
                '/flwr.proto.ServerAppIo/CreateRun',
                request_serializer=flwr_dot_proto_dot_run__pb2.CreateRunRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_run__pb2.CreateRunResponse.FromString,
                _registered_method=True)
        self.GetNodes = channel.unary_unary(
                '/flwr.proto.ServerAppIo/GetNodes',
                request_serializer=flwr_dot_proto_dot_serverappio__pb2.GetNodesRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_serverappio__pb2.GetNodesResponse.FromString,
                _registered_method=True)
        self.PushTaskIns = channel.unary_unary(
                '/flwr.proto.ServerAppIo/PushTaskIns',
                request_serializer=flwr_dot_proto_dot_serverappio__pb2.PushTaskInsRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_serverappio__pb2.PushTaskInsResponse.FromString,
                _registered_method=True)
        self.PullTaskRes = channel.unary_unary(
                '/flwr.proto.ServerAppIo/PullTaskRes',
                request_serializer=flwr_dot_proto_dot_serverappio__pb2.PullTaskResRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_serverappio__pb2.PullTaskResResponse.FromString,
                _registered_method=True)
        self.GetRun = channel.unary_unary(
                '/flwr.proto.ServerAppIo/GetRun',
                request_serializer=flwr_dot_proto_dot_run__pb2.GetRunRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_run__pb2.GetRunResponse.FromString,
                _registered_method=True)
        self.GetFab = channel.unary_unary(
                '/flwr.proto.ServerAppIo/GetFab',
                request_serializer=flwr_dot_proto_dot_fab__pb2.GetFabRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fab__pb2.GetFabResponse.FromString,
                _registered_method=True)
        self.PullServerAppInputs = channel.unary_unary(
                '/flwr.proto.ServerAppIo/PullServerAppInputs',
                request_serializer=flwr_dot_proto_dot_serverappio__pb2.PullServerAppInputsRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_serverappio__pb2.PullServerAppInputsResponse.FromString,
                _registered_method=True)
        self.PushServerAppOutputs = channel.unary_unary(
                '/flwr.proto.ServerAppIo/PushServerAppOutputs',
                request_serializer=flwr_dot_proto_dot_serverappio__pb2.PushServerAppOutputsRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_serverappio__pb2.PushServerAppOutputsResponse.FromString,
                _registered_method=True)
        self.UpdateRunStatus = channel.unary_unary(
                '/flwr.proto.ServerAppIo/UpdateRunStatus',
                request_serializer=flwr_dot_proto_dot_run__pb2.UpdateRunStatusRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_run__pb2.UpdateRunStatusResponse.FromString,
                _registered_method=True)
        self.GetRunStatus = channel.unary_unary(
                '/flwr.proto.ServerAppIo/GetRunStatus',
                request_serializer=flwr_dot_proto_dot_run__pb2.GetRunStatusRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_run__pb2.GetRunStatusResponse.FromString,
                _registered_method=True)
        self.PushLogs = channel.unary_unary(
                '/flwr.proto.ServerAppIo/PushLogs',
                request_serializer=flwr_dot_proto_dot_log__pb2.PushLogsRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_log__pb2.PushLogsResponse.FromString,
                _registered_method=True)


class ServerAppIoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRun(self, request, context):
        """Request run_id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNodes(self, request, context):
        """Return a set of nodes
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushTaskIns(self, request, context):
        """Create one or more tasks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullTaskRes(self, request, context):
        """Get task results
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRun(self, request, context):
        """Get run details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFab(self, request, context):
        """Get FAB
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullServerAppInputs(self, request, context):
        """Pull ServerApp inputs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushServerAppOutputs(self, request, context):
        """Push ServerApp outputs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRunStatus(self, request, context):
        """Update the status of a given run
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRunStatus(self, request, context):
        """Get the status of a given run
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushLogs(self, request, context):
        """Push ServerApp logs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerAppIoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRun': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRun,
                    request_deserializer=flwr_dot_proto_dot_run__pb2.CreateRunRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_run__pb2.CreateRunResponse.SerializeToString,
            ),
            'GetNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNodes,
                    request_deserializer=flwr_dot_proto_dot_serverappio__pb2.GetNodesRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_serverappio__pb2.GetNodesResponse.SerializeToString,
            ),
            'PushTaskIns': grpc.unary_unary_rpc_method_handler(
                    servicer.PushTaskIns,
                    request_deserializer=flwr_dot_proto_dot_serverappio__pb2.PushTaskInsRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_serverappio__pb2.PushTaskInsResponse.SerializeToString,
            ),
            'PullTaskRes': grpc.unary_unary_rpc_method_handler(
                    servicer.PullTaskRes,
                    request_deserializer=flwr_dot_proto_dot_serverappio__pb2.PullTaskResRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_serverappio__pb2.PullTaskResResponse.SerializeToString,
            ),
            'GetRun': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRun,
                    request_deserializer=flwr_dot_proto_dot_run__pb2.GetRunRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_run__pb2.GetRunResponse.SerializeToString,
            ),
            'GetFab': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFab,
                    request_deserializer=flwr_dot_proto_dot_fab__pb2.GetFabRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fab__pb2.GetFabResponse.SerializeToString,
            ),
            'PullServerAppInputs': grpc.unary_unary_rpc_method_handler(
                    servicer.PullServerAppInputs,
                    request_deserializer=flwr_dot_proto_dot_serverappio__pb2.PullServerAppInputsRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_serverappio__pb2.PullServerAppInputsResponse.SerializeToString,
            ),
            'PushServerAppOutputs': grpc.unary_unary_rpc_method_handler(
                    servicer.PushServerAppOutputs,
                    request_deserializer=flwr_dot_proto_dot_serverappio__pb2.PushServerAppOutputsRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_serverappio__pb2.PushServerAppOutputsResponse.SerializeToString,
            ),
            'UpdateRunStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRunStatus,
                    request_deserializer=flwr_dot_proto_dot_run__pb2.UpdateRunStatusRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_run__pb2.UpdateRunStatusResponse.SerializeToString,
            ),
            'GetRunStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRunStatus,
                    request_deserializer=flwr_dot_proto_dot_run__pb2.GetRunStatusRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_run__pb2.GetRunStatusResponse.SerializeToString,
            ),
            'PushLogs': grpc.unary_unary_rpc_method_handler(
                    servicer.PushLogs,
                    request_deserializer=flwr_dot_proto_dot_log__pb2.PushLogsRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_log__pb2.PushLogsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flwr.proto.ServerAppIo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('flwr.proto.ServerAppIo', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ServerAppIo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/CreateRun',
            flwr_dot_proto_dot_run__pb2.CreateRunRequest.SerializeToString,
            flwr_dot_proto_dot_run__pb2.CreateRunResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/GetNodes',
            flwr_dot_proto_dot_serverappio__pb2.GetNodesRequest.SerializeToString,
            flwr_dot_proto_dot_serverappio__pb2.GetNodesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PushTaskIns(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/PushTaskIns',
            flwr_dot_proto_dot_serverappio__pb2.PushTaskInsRequest.SerializeToString,
            flwr_dot_proto_dot_serverappio__pb2.PushTaskInsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PullTaskRes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/PullTaskRes',
            flwr_dot_proto_dot_serverappio__pb2.PullTaskResRequest.SerializeToString,
            flwr_dot_proto_dot_serverappio__pb2.PullTaskResResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/GetRun',
            flwr_dot_proto_dot_run__pb2.GetRunRequest.SerializeToString,
            flwr_dot_proto_dot_run__pb2.GetRunResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFab(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/GetFab',
            flwr_dot_proto_dot_fab__pb2.GetFabRequest.SerializeToString,
            flwr_dot_proto_dot_fab__pb2.GetFabResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PullServerAppInputs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/PullServerAppInputs',
            flwr_dot_proto_dot_serverappio__pb2.PullServerAppInputsRequest.SerializeToString,
            flwr_dot_proto_dot_serverappio__pb2.PullServerAppInputsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PushServerAppOutputs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/PushServerAppOutputs',
            flwr_dot_proto_dot_serverappio__pb2.PushServerAppOutputsRequest.SerializeToString,
            flwr_dot_proto_dot_serverappio__pb2.PushServerAppOutputsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateRunStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/UpdateRunStatus',
            flwr_dot_proto_dot_run__pb2.UpdateRunStatusRequest.SerializeToString,
            flwr_dot_proto_dot_run__pb2.UpdateRunStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRunStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/GetRunStatus',
            flwr_dot_proto_dot_run__pb2.GetRunStatusRequest.SerializeToString,
            flwr_dot_proto_dot_run__pb2.GetRunStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PushLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/flwr.proto.ServerAppIo/PushLogs',
            flwr_dot_proto_dot_log__pb2.PushLogsRequest.SerializeToString,
            flwr_dot_proto_dot_log__pb2.PushLogsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
