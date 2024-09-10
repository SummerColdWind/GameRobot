from plugins.interface import PluginInterface

from plugins.mouse.mouse import mouse_methods

import inspect


class Plugin(PluginInterface):
    def __repr__(self):
        return 'A plugin that calls win32API to simulate mouse events'

    def perform(self, command):
        match command:
            case {'type': str(mouse_method), **rest}:
                if mouse_method in mouse_methods:
                    sig = inspect.signature(mouse_methods[mouse_method])
                    __pos = rest.get('pos', (0, 0))
                    __pos2 = rest.get('pos2', (0, 0))
                    __button = rest.get('button', 'left')
                    __handle = rest.get('handle', '__handle')
                    __duration = rest.get('duration', 10)
                    __delay = rest.get('delay', 10)

                    handle = self.robot.vars.get(__handle)
                    if handle:
                        local_vars = locals()
                        params = {k: local_vars[f'_{type(self).__name__}__{k}']
                                  for k in sig.parameters.keys()}
                        params['handle'] = handle
                        mouse_methods[mouse_method](**params)
                else:
                    raise RuntimeError

            case _:
                raise RuntimeError
