import win32gui
import win32con
import time


MOUSE_EVENTS = {
    'left': (win32con.WM_LBUTTONDOWN, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON),
    'right': (win32con.WM_RBUTTONDOWN, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON),
    'middle': (win32con.WM_MBUTTONDOWN, win32con.WM_MBUTTONUP, win32con.MK_MBUTTON),
}

mouse_methods = {}

def register(func):
    mouse_methods[func.__name__] = func
    return func


def make_lparam(pos):
    x, y = pos
    return y << 16 | x


@register
def mouse_move(handle, pos):
    """ 移动鼠标 """
    lparam = make_lparam(pos)
    win32gui.SendMessage(handle, win32con.WM_MOUSEMOVE, None, lparam)



@register
def mouse_press(handle, pos, button='left', duration=1000):
    """ 按住鼠标 """
    lparam = make_lparam(pos)
    down_msg, up_msg, btn_flag = MOUSE_EVENTS[button]
    win32gui.SendMessage(handle, down_msg, btn_flag, lparam)
    time.sleep(duration / 1000)
    win32gui.SendMessage(handle, up_msg, None, lparam)


@register
def mouse_click(handle, pos, button='left'):
    """ 单击 """
    mouse_press(handle, pos, button, duration=10)

@register
def mouse_double_click(handle, pos, button='left', delay=10):
    """ 双击 """
    mouse_click(handle, pos, button)
    time.sleep(delay / 1000)
    mouse_click(handle, pos, button)


@register
def mouse_drag(handle, pos, pos2, button='left', duration=10):
    """ 匀速拖拽 """
    delta_x, delta_y = pos2[0] - pos[0], pos2[1] - pos[1]
    lparam = make_lparam(pos)
    down_msg, up_msg, btn_flag = MOUSE_EVENTS[button]
    win32gui.SendMessage(handle, down_msg, btn_flag, lparam)
    for i in range(1, int(duration / 10) + 1):
        lparam2 = make_lparam((pos[0] + delta_x * i, pos[1] + delta_y * i))
        win32gui.SendMessage(handle, win32con.WM_MOUSEMOVE, btn_flag, lparam2)
    lparam2 = make_lparam(pos2)
    win32gui.SendMessage(handle, win32con.WM_MOUSEMOVE, btn_flag, lparam2)

    win32gui.SendMessage(handle, up_msg, None, lparam2)

