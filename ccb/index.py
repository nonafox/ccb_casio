from casioplot import *
from gint import *
from imgs.bg import *
from conf import *
from funcs import *
import math

load_data()
load_log()

is_letter_mode = False
is_hint_showing = False
command = ''
log_selected = - 1
sum_selected = - 1
page = 0
sum_data = []

dclear(C_WHITE)
dimage(0, 0, img_bg)
dupdate()

def update_command():
  global is_letter_mode, is_hint_showing, command, log_selected, sum_selected, page, sum_data
  text(0, 0, 'A' if is_letter_mode else '', RGB_WHITE, FONT_SMALL)
  command_to_show, is_cut = cut_toolong_text(command)
  text(.5, .93, command_to_show, RGB_WHITE)
  status = ''
  if is_cut:
    status = '<'
  elif is_hint_showing:
    status = '#'
  text(3, .93, status, RGB_WHITE, FONT_SMALL)

def update_log(jump_to_tail = False):
  global is_letter_mode, is_hint_showing, command, log_selected, sum_selected, page, sum_data
  if page != 0:
    page = 0
    return update_page()
  if jump_to_tail or log_selected < 0 or log_selected >= len(LOG):
    log_selected = len(LOG) - 1
  top = 0
  i0 = (math.ceil((log_selected + 1) / 5) - 1) * 5
  log_selected_found = False
  for i in range(5):
    real_i = i0 + i
    if real_i < 0 or real_i >= len(LOG):
      text(.5, top, '', RGB_BLACK)
      top += 10
      continue
    line = LOG[real_i]
    selected_note = '  '
    if real_i == log_selected:
      selected_note = '> '
      log_selected_found = True
    if line == '':
      pass
    elif line[0] == '$':
      text(.5, top, f'{selected_note}{CASH_PLACEHOLDER}{LIST_SPLIT}{line[1 : ]}', RGB_BLACK)
    elif '$' in line:
      id, money = line.split('$', 1)
      if id in DATA['dict']:
        id = f'({DATA['dict'][id]})'
      text(.5, top, f'{selected_note}{id}{LIST_SPLIT}{money}', RGB_BLACK)
    elif line[0] == '#':
      text(.5, top, f'{selected_note}# {line[1 : ]} #', RGB_BLACK)
    top += 10
  if not log_selected_found:
    log_selected = len(LOG) - 1

    
def update_sum():
  global is_letter_mode, is_hint_showing, command, log_selected, sum_selected, page, sum_data
  if page != 1:
    page = 1
    return update_page()
  sum_data = [
    f'cash count{LIST_SPLIT}{DATA['cash_count']}',
    f'credit count{LIST_SPLIT}{DATA['credit_count']}',
    f'cash{LIST_SPLIT}{money_stringify(DATA['cash'])}',
    f'credit{LIST_SPLIT}{money_stringify(DATA['credit_sum'])}',
    f'sum{LIST_SPLIT}{money_stringify(DATA['cash'] + DATA['credit_sum'])}',
    '# credit list #',
  ]
  for id, money in DATA['credit'].items():
    if id in DATA['dict']:
      id = f'({DATA['dict'][id]})'
    sum_data.append(f'{id}{LIST_SPLIT}{money_stringify(money)}')
  if sum_selected < 0 or sum_selected >= len(sum_data):
    sum_selected = len(sum_data) - 1
  top = 0
  i0 = (math.ceil((sum_selected + 1) / 5) - 1) * 5
  sum_selected_found = False
  for i in range(5):
    real_i = i0 + i
    if real_i < 0 or real_i >= len(sum_data):
      text(.5, top, '', RGB_BLACK)
      top += 10
      continue
    line = sum_data[real_i]
    selected_note = '  '
    if real_i == sum_selected:
      selected_note = '> '
      sum_selected_found = True
    text(.5, top, f'{selected_note}{line}', RGB_BLACK)
    top += 10
  if not sum_selected_found:
    sum_selected = len(sum_data) - 1

def update_page():
  global page
  if page == 0:
    update_log()
    update_command()
    dupdate()
  else:
    update_sum()
    update_command()
    dupdate()
update_page()

def update_data():
  save_data()
  save_log()

while True:
  key = wait_any_key()
  if is_hint_showing:
    command = ''
    is_hint_showing = False
  else:
    if key == KEY_EXE:
      if '..' in command:
        try:
          id, equa = command.split('..', 1)
          money = money_numeric(eval(equa))
          if id not in DATA['credit']:
            DATA['credit'][id] = 0
          DATA['credit'][id] += money
          DATA['credit_sum'] += money
          DATA['credit_count'] += 1
          LOG.append(f'{id}${money_stringify(money)}')
          update_data()
          update_log(True)
          command = ''
        except:
          command = 'wrong command'
          is_hint_showing = True
      elif '--' in command:
        try:
          id, name = command.split('--', 1)
          if name != '':
            DATA['dict'][id] = name
          elif id in DATA['dict']:
            del DATA['dict'][id]
          update_data()
          update_log()
          command = ''
        except:
          command = 'wrong command'
          is_hint_showing = True
      elif command[0 : 2] == '++':
        LOG.append(f'#{command[2 : ]}')
        update_data()
        update_log(True)
        command = ''
      elif command == 'delete':
        if log_selected >= 0 and log_selected < len(LOG):
          if LOG[log_selected] == '':
            pass
          elif LOG[log_selected][0] == '$':
            DATA['cash'] -= money_numeric(LOG[log_selected][1 : ])
            DATA['cash_count'] -= 1
            del LOG[log_selected]
          elif '$' in LOG[log_selected]:
            id, money = LOG[log_selected].split('$', 1)
            money = money_numeric(money)
            DATA['credit'][id] -= money
            DATA['credit_sum'] -= money
            DATA['credit_count'] -= 1
            del LOG[log_selected]
          elif LOG[log_selected][0] == '#':
            del LOG[log_selected]
        update_data()
        update_log()
        command = ''
      else:
        try:
          money = money_numeric(eval(command))
          DATA['cash'] += money
          DATA['cash_count'] += 1
          LOG.append(f'${money_stringify(money)}')
          update_data()
          update_log(True)
          command = ''
        except:
          command = 'wrong command'
          is_hint_showing = True
    elif key == KEY_DEL:
      command = command[0 : - 1]
    elif key == KEY_SHIFT:
      is_letter_mode = not is_letter_mode
    elif key == KEY_UP:
      if page == 0:
        if log_selected > 0:
          log_selected -= 1
      elif page == 1:
        if sum_selected > 0:
          sum_selected -= 1
      update_page()
    elif key == KEY_DOWN:
      if page == 0:
        if log_selected < len(LOG) - 1:
          log_selected += 1
      elif page == 1:
        if sum_selected < len(sum_data) - 1:
          sum_selected += 1
      update_page()
    elif key == KEY_LEFT:
      page = 0
      update_page()
    elif key == KEY_RIGHT:
      page = 1
      update_page()
    else:
      command += translate_key(is_letter_mode, key)
  update_command()
  dupdate()
