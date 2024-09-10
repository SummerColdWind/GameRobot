import os
import sys
from threading import Thread
from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog, QListWidget, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon

from ui.utils.output import OutputStream
from robot.bot import GameRobot


class BotUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), 'botui.ui'), self)
        sys.stdout = OutputStream(self.output)
        self.bot = GameRobot()
        self.thread = Thread()
        self.lines = []
        self.init()

    def init(self):
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), 'icon.png')))

        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.load_bot_code)
        self.actionRun.setShortcut("Ctrl+R")
        self.actionRun.triggered.connect(self.run_code)
        self.actionRun_selected.setShortcut("Ctrl+Return")
        self.actionRun_selected.triggered.connect(self.run_code_selected)
        self.variables_timer = QTimer()
        self.variables_timer.timeout.connect(self.update_variables)
        self.variables_timer.start(1000)

        print('Initialization complete.')

    def update_statements(self):
        self.statements.clear()
        for line in self.lines:
            self.statements.addItem(line.rstrip('\n'))

    def update_variables(self):
        self.variables.clear()
        for key, value in self.bot.vars.items():
            if not isinstance(value, (str, int, float, tuple, list)):
                value = type(value).__name__
            self.variables.addItem(f'[{key}] {repr(value)}')

    def load_bot_code(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        with open(file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()
        self.update_statements()
        print(f'Load bot code from {file_path}')

    def run(self):
        if self.thread.is_alive():
            print('Bot thread already running')
            return
        self.thread = Thread(target=self.bot.do)
        self.thread.start()

    def run_code(self):
        self.bot.read(self.lines)
        self.run()

    def run_code_selected(self):
        lines = [self.lines[i.row()] for i in self.statements.selectedIndexes()]
        self.bot.read(lines)
        self.run()

