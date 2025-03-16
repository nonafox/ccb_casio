from casioplot import *
from gint import *

RGB_WHITE = (255, 255, 255)
RGB_BLACK = (0, 0, 0)

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
SCREEN_SIZES = [SCREEN_WIDTH, SCREEN_HEIGHT]

FONT_MARGIN_WIDTH = 1
FONT_SIZES = {
  'small': [3, 5],
  'medium': [4, 6],
  'large': [5, 7],
}
FONT_SMALL = 'small'
FONT_MEDIUM = 'medium'
FONT_LARGE = 'large'
TEXT_TOOLONG_LENGTH = 17

KEYS_TABLE_LETTERS = {
  KEY_XOT: 'a',
  KEY_LOG: 'b',
  KEY_LN: 'c',
  KEY_SIN: 'd',
  KEY_COS: 'e',
  KEY_TAN: 'f',
  KEY_FRAC: 'g',
  KEY_SWITCH: 'h',
  KEY_LEFTP: 'i',
  KEY_RIGHTP: 'j',
  KEY_COMMA: 'k',
  KEY_ARROW: 'l',
  KEY_7: 'm',
  KEY_8: 'n',
  KEY_9: 'o',
  KEY_4: 'p',
  KEY_5: 'q',
  KEY_6: 'r',
  KEY_TIMES: 's',
  KEY_DIV: 't',
  KEY_1: 'u',
  KEY_2: 'v',
  KEY_3: 'w',
  KEY_PLUS: 'x',
  KEY_MINUS: 'y',
  KEY_0: 'z',
  KEY_DOT: ' ',
}
KEYS_TABLE_NUMBERS = {
  KEY_7: '7',
  KEY_8: '8',
  KEY_9: '9',
  KEY_4: '4',
  KEY_5: '5',
  KEY_6: '6',
  KEY_MUL: '*',
  KEY_DIV: '/',
  KEY_1: '1',
  KEY_2: '2',
  KEY_3: '3',
  KEY_PLUS: '+',
  KEY_MINUS: '-',
  KEY_0: '0',
  KEY_DOT: '.',
}

MONEY_DIGIT = 1
CASH_PLACEHOLDER = '---'
LIST_SPLIT = '   '

FILE_DATA = 'ccb/data/data.json'
FILE_LOG = 'ccb/data/log.txt'

# template
DATA = {
  'cash': 0,
  'credit_sum': 0,
  "cash_count": 0,
  "credit_count": 4,
  'credit': {
    'id': 0,
  },
  'dict': {
    'id': 'name'
  }
}
LOG = [
  ''
]
