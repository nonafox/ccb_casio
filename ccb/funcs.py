from casioplot import *
from gint import *
from conf import *

def translate_key(key: int):
  if key in KEYS_TABLE:
    return KEYS_TABLE[key]
  else:
    return ''
