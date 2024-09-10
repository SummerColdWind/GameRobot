from plugins.interface import PluginInterface

from plugins.keyboard.keyboard import keyboard_methods

import inspect

class Plugin(PluginInterface):
    def __repr__(self):
        return 'A plugin that calls win32API to simulate keyborad events'

    def perform(self, command):
        match command:
            case {'type': str(keyboard_method), **rest}:
                if keyboard_method in keyboard_methods:
                    sig = inspect.signature(keyboard_methods[keyboard_method])
                    __key = rest.get('key', 'enter')
                    __text = rest.get('text', '')
                    __handle = rest.get('handle', '__handle')
                    __duration = rest.get('duration', 10)

                    handle = self.robot.vars.get(__handle)
                    if handle:
                        local_vars = locals()
                        params = {k: local_vars[f'_{type(self).__name__}__{k}']
                                  for k in sig.parameters.keys()}
                        params['handle'] = handle
                        keyboard_methods[keyboard_method](**params)
                else:
                    raise RuntimeError

            case _:
                raise RuntimeError
