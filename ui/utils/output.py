import datetime
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QTextCursor
import traceback
import sys

TIME_COLOR = 'gray'
ERROR_COLOR = 'red'

def excepthook(exc_type, exc_value, exc_traceback):
    error_message = "Uncaught exception: " + exc_type.__name__
    print(f'<span style="color:{ERROR_COLOR};">{error_message}</span>')
    traceback.print_exception(exc_type, exc_value, exc_traceback)


sys.excepthook = excepthook


class OutputStream(QObject):
    def __init__(self, text_browser):
        super().__init__()
        self.text_browser = text_browser

    def write(self, text):
        if text.strip():  # 仅在有内容时附加时间戳
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_text = f'<span style="color:{TIME_COLOR};">[{current_time}]</span> {text}\n'
            self.text_browser.append(formatted_text)
            self.text_browser.moveCursor(QTextCursor.MoveOperation.End)

    def flush(self):
        pass
