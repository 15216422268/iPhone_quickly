from pynput import keyboard

import mouse_ctrl as mc
import keyboard_mappings as km
import game_board as gb


# 按键按下
def on_press(key):
    # '按下按键时执行。'
    # print('on_press: ', key)
    try:
        if not gb.is_iphone():
            return
        move_dist = km.move_down_mappings.get(key)
        if move_dist is not None:
            move_dist()
            return

    except AttributeError as e:
        print('on_press key {0} pressed'.format(key), e)
    # 通过属性判断按键类型。


# 按键抬起
def on_release(key):
    # '松开按键时执行。'
    # print('on_release: ', key)
    try:
        if not gb.is_iphone():
            return
        if key == keyboard.Key.esc:
            return False

        move_dist = km.move_up_mappings.get(key)
        if move_dist is not None:
            move_dist()
            return

        if key.char == '0':
            mc.get_pos()
            return

        key_up = key.char
        click_pos = km.key_mappings.get(key_up)
        if click_pos is None:
            return
        click_pos()
    except AttributeError as e:
        print('on_release key {0} pressed'.format(key), e)


def keyboard_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
