# (c) @ballicipluck

from base64 import b64encode, b64decode


def str_to_b64(str):
  str_bytes = str.encode('ascii')
  bytes_b64= b64encode(str_bytes)
  b64 = bytes_b64.decode('ascii')
  return b64


def b64_to_str(b64):
  bytes_b64 = b64.encode('ascii')
  bytes_str = b64decode(bytes_b64)
  str = bytes_str.decode('ascii')
  return str 
