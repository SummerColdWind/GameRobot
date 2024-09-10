from plugins.interface import PluginInterface

import sys
import time

class Plugin(PluginInterface):
    def __repr__(self):
        return 'Base Plugin'

    def perform(self, command):
        match command:
            case {'type': 'exec', 'then': [*statements]}:
                exec(''.join(statements), self.robot.vars)
            case {'type': 'pass'}:
                pass
            case {'type': 'print', 'text': text}:
                print(text)
            case {'type': 'set', 'name': str(name), 'value': value}:
                self.robot.vars[name] = value
            case {'type': 'sleep', 'duration': int(duration)}:
                time.sleep(duration / 1000)
            case {'type': 'exit'}:
                sys.exit(0)
            case {'type': 'if', 'condition': var, 'then': [*statements], 'else': [*statements_else]}:
                if var:
                    self.robot.do(statements)
                else:
                    self.robot.do(statements_else)
            case {'type': 'while', 'name': name, 'then': [*statements]}:
                while self.robot.vars.get(name):
                    self.robot.do(statements)
            case {'type': 'for', 'times': int(times), 'then': [*statements]}:
                for i in range(times):
                    self.robot.do(statements)
            case _:
                raise RuntimeError
