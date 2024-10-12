import sys
from ui.ui import BotUI
from PyQt6.QtWidgets import QApplication

import win32gui, win32con, win32ui, win32api
import PIL
from PIL import Image
import tkinter
from tkinter import ttk

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BotUI()
    window.show()
    sys.exit(app.exec())
