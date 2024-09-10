from __future__ import annotations

import win32con
import win32gui

from dataclasses import dataclass


filter_methods = {}


def register(func):
    filter_methods[func.__name__] = func
    return func


def get_all_handles():
    """获取当前所有窗口的句柄"""
    parent_hwnd_list = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), parent_hwnd_list)
    return parent_hwnd_list

def get_current_handle():
    """获取当前最前置窗口的句柄"""
    handle = win32gui.GetForegroundWindow()
    return handle

def get_child_handles(parent_handle):
    """获取指定父窗口句柄的所有子窗口句柄"""
    child_hwnd_list = []
    win32gui.EnumChildWindows(parent_handle, lambda hwnd, param: param.append(hwnd), child_hwnd_list)
    return child_hwnd_list

def get_title(handle):
    """获取窗口的标题"""
    return win32gui.GetWindowText(handle)

def get_cls(handle):
    """获取窗口的类名"""
    return win32gui.GetClassName(handle)

def get_pos(handle):
    """获取窗口位置参数，返回 (left, top, right, bottom)"""
    rect = win32gui.GetWindowRect(handle)
    left, top, right, bottom = rect
    return left, top, right, bottom

def get_rect(handle):
    """获取窗口矩形，返回 (width, height)"""
    left, top, right, bottom = get_pos(handle)
    width = right - left
    height = bottom - top
    return width, height


@register
def filter_handle_by_title(title, parent=None):
    """根据窗口标题过滤句柄"""
    if parent is None:
        return set(h for h in get_all_handles() if get_title(h) == title)
    return set(h for h in get_child_handles(parent) if get_title(h) == title)

@register
def filter_handle_by_cls(cls, parent=None):
    """根据窗口类名过滤句柄"""
    if parent is None:
        return set(h for h in get_all_handles() if get_cls(h) == cls)
    return set(h for h in get_child_handles(parent) if get_cls(h) == cls)

@register
def filter_handle_by_title_part(title_part, parent=None):
    """根据部分窗口标题过滤句柄"""
    if parent is None:
        return set(h for h in get_all_handles() if title_part in get_title(h))
    return set(h for h in get_child_handles(parent) if title_part in get_title(h))

@register
def filter_handle_by_cls_part(cls_part, parent=None):
    """根据部分窗口类名过滤句柄"""
    if parent is None:
        return set(h for h in get_all_handles() if cls_part in get_cls(h))
    return set(h for h in get_child_handles(parent) if cls_part in get_cls(h))

@register
def filter_handle_by_width(width, parent=None):
    """根据窗口宽度过滤句柄"""
    if parent is None:
        return set(h for h in get_all_handles() if get_rect(h)[0] == int(width))
    return set(h for h in get_child_handles(parent) if get_rect(h)[0] == int(width))

@register
def filter_handle_by_height(height, parent=None):
    """根据窗口高度过滤句柄"""
    if parent is None:
        return set(h for h in get_all_handles() if get_rect(h)[1] == int(height))
    return set(h for h in get_child_handles(parent) if get_rect(h)[1] == int(height))








