
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/string_int_label_map.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n2object_detection/protos/string_int_label_map.proto\x12\x17object_detection.protos\"G\n\x15StringIntLabelMapItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\"Q\n\x11StringIntLabelMap\x12<\n\x04item\x18\x01 \x03(\x0b\x32..object_detection.protos.StringIntLabelMapItem')
)




_STRINGINTLABELMAPITEM = _descriptor.Descriptor(
  name='StringIntLabelMapItem',
  full_name='object_detection.protos.StringIntLabelMapItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='object_detection.protos.StringIntLabelMapItem.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='object_detection.protos.StringIntLabelMapItem.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='object_detection.protos.StringIntLabelMapItem.display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=150,
)


_STRINGINTLABELMAP = _descriptor.Descriptor(
  name='StringIntLabelMap',
  full_name='object_detection.protos.StringIntLabelMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='object_detection.protos.StringIntLabelMap.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=233,
)

_STRINGINTLABELMAP.fields_by_name['item'].message_type = _STRINGINTLABELMAPITEM
DESCRIPTOR.message_types_by_name['StringIntLabelMapItem'] = _STRINGINTLABELMAPITEM
DESCRIPTOR.message_types_by_name['StringIntLabelMap'] = _STRINGINTLABELMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringIntLabelMapItem = _reflection.GeneratedProtocolMessageType('StringIntLabelMapItem', (_message.Message,), dict(
  DESCRIPTOR = _STRINGINTLABELMAPITEM,
  __module__ = 'object_detection.protos.string_int_label_map_pb2'

  ))
_sym_db.RegisterMessage(StringIntLabelMapItem)

StringIntLabelMap = _reflection.GeneratedProtocolMessageType('StringIntLabelMap', (_message.Message,), dict(
  DESCRIPTOR = _STRINGINTLABELMAP,
  __module__ = 'object_detection.protos.string_int_label_map_pb2'

  ))
_sym_db.RegisterMessage(StringIntLabelMap)


