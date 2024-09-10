from plugins.interface import PluginInterface


class Plugin(PluginInterface):
    def __repr__(self):
        return 'A plugin for smart operation'

    def perform(self, command):
        match command:
            case {'type': 'click_until', 'pos': (x, y), **rest}:
                __handle = rest.get('handle', '__handle')
                __delay = rest.get('delay', 1000)
                __period = rest.get('period', 10)
                __rgb = rest.get('rgb')
                __image = rest.get('image')

                if pos2 := rest.get('pos2') is not None:
                    x, y = pos2

                if __rgb is not None:
                    while True:
                        self.robot.do([
                            {'type': 'pixel', 'pos': (x, y), 'handle': __handle}
                        ])
                        rgb = self.robot.vars['__last_pixel']
                        if all(m == n for m, n in zip(rgb, __rgb)):
                            self.robot.do([
                                {'type': 'click', 'pos': (x, y), 'handle': __handle, 'period': __period}
                            ])
                            break
                        else:
                            self.robot.do([
                                {'type': 'sleep', 'delay': __delay}
                            ])

                if __image is not None:
                    while True:
                        self.robot.do([
                            {'type': 'templ', 'image': __image, 'handle': __handle}
                        ])
                        center = self.robot.vars['__last_templ']
                        if center:
                            x, y = center
                            self.robot.do([
                                {'type': 'click', 'pos': (x, y), 'handle': __handle, 'period': __period}
                            ])
                            break
                        else:
                            self.robot.do([
                                {'type': 'sleep', 'delay': __delay}
                            ])

            case _:
                raise RuntimeError
