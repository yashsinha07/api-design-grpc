# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventoryservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16inventoryservice.proto\"g\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0c\n\x04year\x18\x04 \x01(\x05\x12\x1a\n\x05genre\x18\x05 \x01(\x0e\x32\x06.GenreH\x00\x88\x01\x01\x42\x08\n\x06_genre\"t\n\rInventoryItem\x12\x17\n\x0finventoryNumber\x18\x01 \x01(\x05\x12\x12\n\x01\x62\x18\x02 \x01(\x0b\x32\x05.BookH\x00\x12\x1c\n\x06status\x18\x03 \x01(\x0e\x32\x07.StatusH\x01\x88\x01\x01\x42\r\n\x0b\x62ook_one_ofB\t\n\x07_status\"(\n\x11\x43reateBookRequest\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book\"(\n\x12\x43reateBookResponse\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"&\n\x0fGetBookResponse\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book*0\n\x05Genre\x12\x0b\n\x07ROMANCE\x10\x00\x12\r\n\tBIOGRAPHY\x10\x01\x12\x0b\n\x07\x46ICTION\x10\x02*\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x32{\n\x10InventoryService\x12\x37\n\nCreateBook\x12\x12.CreateBookRequest\x1a\x13.CreateBookResponse\"\x00\x12.\n\x07GetBook\x12\x0f.GetBookRequest\x1a\x10.GetBookResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventoryservice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=405
  _GENRE._serialized_end=453
  _STATUS._serialized_start=455
  _STATUS._serialized_end=489
  _BOOK._serialized_start=26
  _BOOK._serialized_end=129
  _INVENTORYITEM._serialized_start=131
  _INVENTORYITEM._serialized_end=247
  _CREATEBOOKREQUEST._serialized_start=249
  _CREATEBOOKREQUEST._serialized_end=289
  _CREATEBOOKRESPONSE._serialized_start=291
  _CREATEBOOKRESPONSE._serialized_end=331
  _GETBOOKREQUEST._serialized_start=333
  _GETBOOKREQUEST._serialized_end=363
  _GETBOOKRESPONSE._serialized_start=365
  _GETBOOKRESPONSE._serialized_end=403
  _INVENTORYSERVICE._serialized_start=491
  _INVENTORYSERVICE._serialized_end=614
# @@protoc_insertion_point(module_scope)
