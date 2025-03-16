from casioplot import *
from gint import *
from conf import *

my_texts = {}

def color_invert(color: tuple[int, int, int]):
  if color == RGB_BLACK:
    return RGB_WHITE
  return RGB_BLACK

def wait_key(key: int):
  cleareventflips()
  clearevents()
  while 1:
    ev = pollevent()
    if ev.type == KEYEV_DOWN and ev.key == key:
      break
def wait_any_key():
  cleareventflips()
  clearevents()
  while 1:
    ev = pollevent()
    if ev.type == KEYEV_DOWN:
      return ev.key
def translate_key(is_letter: bool, key: int):
  table = KEYS_TABLE_LETTERS if is_letter else KEYS_TABLE_NUMBERS
  if key in table:
    return table[key]
  else:
    return ''

def calc_text_pos(axis: int, offset: int, text: str, size: str):
  n = len(text)
  if axis == 0:
    return int((SCREEN_SIZES[0] - n * FONT_SIZES[size][0] - FONT_MARGIN_WIDTH * (n - 1)) * offset)
  else:
    return int((SCREEN_SIZES[1] - FONT_SIZES[size][1]) * offset)

def cut_toolong_text(text: str):
  if len(text) > TEXT_TOOLONG_LENGTH:
    return (text[- TEXT_TOOLONG_LENGTH - 1 : ], True)
  else:
    return (text, False)

def text(x: int, y: int, text: str, color: tuple[int, int, int] = RGB_BLACK, size: str = FONT_LARGE):
  x1, y1 = x, y
  if 0 < x < 1:
    x1 = calc_text_pos(0, x, text, size)
  if 0 < y < 1:
    y1 = calc_text_pos(1, y, text, size)
  my_text_profile = [x1, y1, text, color, size]
  if (x, y) in my_texts:
    profile = my_texts[x, y]
    if profile != my_text_profile:
      draw_string(profile[0], profile[1], profile[2], color_invert(profile[3]), profile[4])
    del my_texts[x, y]
  draw_string(x1, y1, text, color, size)
  my_texts[x, y] = my_text_profile

def load_data():
  with open(FILE_DATA, 'r') as f:
    DATA.clear()
    DATA.update(dict(eval(f.read())))
def save_data():
  with open(FILE_DATA, 'w') as f:
    f.write(str(DATA))
def load_log():
  with open(FILE_LOG, 'r') as f:
    LOG.clear()
    LOG.extend(f.read().split('\n'))
def save_log():
  with open(FILE_LOG, 'w') as f:
    f.write('\n'.join(LOG))

def money_numeric(text: str):
  return round(float(text), MONEY_DIGIT)
def money_stringify(num: float | str):
  num = money_numeric(num)
  if num < 0:
    return str(num)
  else:
    return '+' + str(num)
