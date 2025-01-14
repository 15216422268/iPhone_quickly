import time

import Quartz.CoreGraphics as CG
import keyboard_mappings as km

flag = False


# 模拟鼠标按下
def mouse_down(pos):
    # print("mouse_down", pos)
    event = CG.CGEventCreateMouseEvent(None, CG.kCGEventLeftMouseDown, pos, CG.kCGMouseButtonLeft)
    # 发送事件到系统（后台点击）
    CG.CGEventPost(CG.kCGHIDEventTap, event)

    global flag
    if not flag:
        flag = True


# 模拟鼠标松开
def mouse_up(pos):
    # print("mouse_up", pos)
    event = CG.CGEventCreateMouseEvent(None, CG.kCGEventLeftMouseUp, pos, CG.kCGMouseButtonLeft)
    CG.CGEventPost(CG.kCGHIDEventTap, event)

    global flag
    if flag:
        flag = False


# 模拟鼠标移动
def move_mouse(pos):
    event = CG.CGEventCreateMouseEvent(None, CG.kCGEventLeftMouseDragged, pos, CG.kCGMouseButtonLeft)
    CG.CGEventPost(CG.kCGHIDEventTap, event)


# 模拟点击
def click(pos):
    mouse_down(pos)
    mouse_up(pos)


def reverse(pos):
    return tuple(-x for x in pos)


def add(*t):
    return tuple(map(lambda *p: sum(p), *t))


def div(pos, div):
    return tuple(o / div for o in pos)


def mul(pos, mul):
    return tuple(o * mul for o in pos)


# 模拟拖动
def move(pos1, pos2):
    mouse_down(pos1)
    # 拖动时的分步数
    steps = 30
    # 计算拖动的步长
    pos = div(add(pos2, reverse(pos1)), steps)
    # 创建鼠标拖动事件
    for i in range(steps):
        move_mouse(add(pos1, mul(pos, i)))
        time.sleep(0.1 / steps)  # 控制拖动速度
    mouse_up(pos2)


def get_pos():
    # 获取鼠标的当前位置
    mouse_event = CG.CGEventCreate(None)
    mouse_location = CG.CGEventGetLocation(mouse_event)
    print('pos: ', add((mouse_location.x, mouse_location.y), reverse(km.POS)))
