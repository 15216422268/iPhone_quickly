import mouse_ctrl as mc

from pynput import keyboard
import game_board as gb
import numpy as np

flag = False

windows = gb.get_windows_with_title()
print(windows)
gb.activate_window()

POS = (windows['X'], windows['Y'])


def add(*t):
    return tuple(map(lambda *p: sum(p), *t))


def skill_click(pos, threshold = 20):
    mc.click(add(POS, get_random(pos, threshold)))


def get_random(pos, threshold=18):
    a = np.random.normal(loc =0.0 , scale= 6.0,size = (1,2))
    if -threshold < a[0][0] < threshold or -threshold < a[0][1] < threshold  :
        return add(pos, (a[0][0], a[0][1]))
    return get_random(pos, threshold)


# 拖动按键
button_attr = {
    # 摇杆
    'joystick': {
        'center': (160, 360),
        'up': (0, -50),
        'down': (0, 50),
        'left': (-50, 0),
        'right': (50, 0),
    },
    # 基础攻击
    'base': {
        'center': (835, 395),
        'up': (0, -50),
        'down': (0, 50),
        'left': (-50, 0),
        'right': (50, 0),
    },
    # 滑动技能
    'skill': {
        'center': (782, 227),
        'up': (0, -35),
        'down': (0, 35),
        'left': (-35, 0),
        'right': (35, 0),
    },
}

move_pos = {
    'up': add(POS, button_attr['joystick']['center'], button_attr['joystick']['up']),
    'down': add(POS, button_attr['joystick']['center'], button_attr['joystick']['down']),
    'left': add(POS, button_attr['joystick']['center'], button_attr['joystick']['left']),
    'right': add(POS, button_attr['joystick']['center'], button_attr['joystick']['right']),

    'base_up': {
        'start': add(POS, button_attr['base']['center']),
        'end': add(POS, button_attr['base']['center'], button_attr['base']['up'])
    },
    'base_down': {
        'start': add(POS, button_attr['base']['center']),
        'end': add(POS, button_attr['base']['center'], button_attr['base']['down'])
    },
    'base_left': {
        'start': add(POS, button_attr['base']['center']),
        'end': add(POS, button_attr['base']['center'], button_attr['base']['left'])
    },
    'base_right': {
        'start': add(POS, button_attr['base']['center']),
        'end': add(POS, button_attr['base']['center'], button_attr['base']['right'])
    },

    'skill_up': {
        'start': add(POS, button_attr['skill']['center']),
        'end': add(POS, button_attr['skill']['center'], button_attr['skill']['up'])
    },
    'skill_down': {
        'start': add(POS, button_attr['skill']['center']),
        'end': add(POS, button_attr['skill']['center'], button_attr['skill']['down'])
    },
    'skill_left': {
        'start': add(POS, button_attr['skill']['center']),
        'end': add(POS, button_attr['skill']['center'], button_attr['skill']['left'])
    },
    'skill_right': {
        'start': add(POS, button_attr['skill']['center']),
        'end': add(POS, button_attr['skill']['center'], button_attr['skill']['right'])
    },
}

# 移动
move_down_mappings = {
    keyboard.Key.left: lambda: mc.mouse_down(move_pos['left']),
    keyboard.Key.right: lambda: mc.mouse_down(move_pos['right']),
    keyboard.Key.up: lambda: mc.mouse_down(move_pos['up']),
    keyboard.Key.down: lambda: mc.mouse_down(move_pos['down']),
}

# 移动
move_up_mappings = {
    keyboard.Key.left: lambda: mc.mouse_up(move_pos['left']),
    keyboard.Key.right: lambda: mc.mouse_up(move_pos['right']),
    keyboard.Key.up: lambda: mc.mouse_up(move_pos['up']),
    keyboard.Key.down: lambda: mc.mouse_up(move_pos['down']),
}

# 点击出发技能
key_mappings = {
    # 点击技能
    'x': lambda: skill_click((830, 385)),
    'c': lambda: skill_click((865, 330)),
    'v': lambda: skill_click((770, 415)),

    # 普通技能
    'a': lambda: skill_click((585, 405)),
    's': lambda: skill_click((650, 405)),
    'd': lambda: skill_click((714, 407)),
    'f': lambda: skill_click((735, 340)),
    'g': lambda: skill_click((782, 290)),
    'h': lambda: skill_click((850, 270)),
    'b': lambda: skill_click((850, 210)),

    # 扩展技能栏
    'q': lambda: skill_click((720, 165)),
    'w': lambda: skill_click((760, 165)),
    'e': lambda: skill_click((805, 165)),
    'r': lambda: skill_click((850, 165)),

    # 普通攻击滑动技能
    'z': lambda: mc.move(move_pos['base_up']['start'], move_pos['base_up']['end']),
    '.': lambda: mc.move(move_pos['base_down']['start'], move_pos['base_down']['end']),
    '/': lambda: mc.move(move_pos['base_right']['start'], move_pos['base_right']['end']),

    # 滑动技能
    '1': lambda: mc.move(move_pos['skill_up']['start'], move_pos['skill_up']['end']),
    '2': lambda: mc.move(move_pos['skill_down']['start'], move_pos['skill_down']['end']),
    '3': lambda: mc.move(move_pos['skill_left']['start'], move_pos['skill_left']['end']),
    '4': lambda: mc.move(move_pos['skill_right']['start'], move_pos['skill_right']['end']),
}
