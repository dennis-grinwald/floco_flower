# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: flwr/proto/grpcadapter.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'flwr/proto/grpcadapter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66lwr/proto/grpcadapter.proto\x12\nflwr.proto\"\xba\x01\n\x10MessageContainer\x12<\n\x08metadata\x18\x01 \x03(\x0b\x32*.flwr.proto.MessageContainer.MetadataEntry\x12\x19\n\x11grpc_message_name\x18\x02 \x01(\t\x12\x1c\n\x14grpc_message_content\x18\x03 \x01(\x0c\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32Z\n\x0bGrpcAdapter\x12K\n\x0bSendReceive\x12\x1c.flwr.proto.MessageContainer\x1a\x1c.flwr.proto.MessageContainer\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.grpcadapter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGECONTAINER_METADATAENTRY']._loaded_options = None
  _globals['_MESSAGECONTAINER_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_MESSAGECONTAINER']._serialized_start=45
  _globals['_MESSAGECONTAINER']._serialized_end=231
  _globals['_MESSAGECONTAINER_METADATAENTRY']._serialized_start=184
  _globals['_MESSAGECONTAINER_METADATAENTRY']._serialized_end=231
  _globals['_GRPCADAPTER']._serialized_start=233
  _globals['_GRPCADAPTER']._serialized_end=323
# @@protoc_insertion_point(module_scope)
