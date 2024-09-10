import win32gui
import win32con
import win32api
import time

# 常用虚拟键码 https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
KEY_EVENTS = {
    'enter': win32con.VK_RETURN,
    'esc': win32con.VK_ESCAPE,
    'tab': win32con.VK_TAB,
    'shift': win32con.VK_SHIFT,
    'ctrl': win32con.VK_CONTROL,
    'alt': win32con.VK_MENU,
    'space': win32con.VK_SPACE,
}

keyboard_methods = {}

def register(func):
    keyboard_methods[func.__name__] = func
    return func

@register
def key_press(handle, key, duration=1000):
    """ 按住键盘按键 """
    if key in KEY_EVENTS:
        vk_code = KEY_EVENTS[key]
    else:
        vk_code = ord(key.upper())  # 将字母转换为虚拟键码

    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
    time.sleep(duration / 1000)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, vk_code, 0)

@register
def key_click(handle, key):
    """ 模拟键盘单击 """
    key_press(handle, key, duration=10)

@register
def key_type(handle, text, duration=10):
    """ 模拟键入一串字符 """
    delay = duration / 1000 / len(text)
    for char in text:
        vk_code = ord(char)
        win32gui.SendMessage(handle, win32con.WM_CHAR, vk_code, 0)
        time.sleep(delay)


