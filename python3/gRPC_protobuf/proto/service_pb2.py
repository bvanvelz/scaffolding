# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/service.proto\x12\ttutorials\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2G\n\x07Greeter\x12<\n\x08SayHello\x12\x17.tutorials.HelloRequest\x1a\x15.tutorials.HelloReply\"\x00\x42\x03\x90\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\220\001\001'
  _globals['_HELLOREQUEST']._serialized_start=34
  _globals['_HELLOREQUEST']._serialized_end=62
  _globals['_HELLOREPLY']._serialized_start=64
  _globals['_HELLOREPLY']._serialized_end=93
  _globals['_GREETER']._serialized_start=95
  _globals['_GREETER']._serialized_end=166
_builder.BuildServices(DESCRIPTOR, 'proto.service_pb2', _globals)
# @@protoc_insertion_point(module_scope)
