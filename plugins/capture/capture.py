import cv2
import time
import numpy as np
import win32gui, win32con, win32ui, win32api
from ctypes import windll

windll.user32.SetProcessDPIAware()

def _capture(handle):
    """通过win32方式截图，并且无视硬件加速"""
    rect = win32gui.GetWindowRect(handle)
    width, height = rect[2] - rect[0], rect[3] - rect[1]
    hwnd_dc = win32gui.GetWindowDC(handle)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()
    save_bit_map = win32ui.CreateBitmap()
    save_bit_map.CreateCompatibleBitmap(mfc_dc, width, height)
    save_dc.SelectObject(save_bit_map)
    windll.user32.PrintWindow(handle, save_dc.GetSafeHdc(), 3)
    bmpinfo = save_bit_map.GetInfo()
    bmpstr = save_bit_map.GetBitmapBits(True)
    image = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
    image = np.ascontiguousarray(image)[..., :-1]
    win32gui.DeleteObject(save_bit_map.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(handle, hwnd_dc)
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    return image


def capture(handle):
    while True:
        try:
            image = _capture(handle)
            return image
        except Exception as e:
            print(e)
            time.sleep(100)
            continue


def _pixel(handle, pos):
    """ 获取指定位置像素颜色 """
    x, y = pos
    hdc = win32gui.GetWindowDC(handle)
    color = win32api.GetPixel(hdc, x, y)
    win32gui.ReleaseDC(handle, hdc)
    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    return r, g, b


def pixel(handle, pos):
    while True:
        try:
            rgb = _pixel(handle, pos)
            return rgb
        except Exception as e:
            print(e)
            continue


def show_image(image, wait=0):
    cv2.imshow('Show', image)
    cv2.waitKey(wait)


def save_image(image, path='test.png'):
    cv2.imwrite(path, image)



