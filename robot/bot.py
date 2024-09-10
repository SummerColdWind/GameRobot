import importlib
import os

from robot.read.parser import Parser

plugins_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../plugins'))


class GameRobot:
    __slots__ = ['vars', 'plugins', 'statements', 'parser']

    def __init__(self):
        self.vars = {}
        self.parser = Parser()
        self.statements = []
        self.plugins = {name: importlib.import_module(f'plugins.{name}.plugin').Plugin(self)
                        for name in os.listdir(plugins_dir)
                        if os.path.isdir(os.path.join(plugins_dir, name))
                        and 'plugin.py' in os.listdir(os.path.join(plugins_dir, name))}

    def read(self, path):
        self.statements = self.parser(path)

    def do(self, statements=None):
        for command in self.statements if statements is None else statements:
            _command = {**command}
            for key, value in _command.items():
                if isinstance(value, str) and value.startswith('$'):
                    _command[key] = self.vars.get(value[1:])
            for plugin in self.plugins.values():
                try:
                    plugin.perform(_command)
                except RuntimeError:
                    continue
                else:
                    break


