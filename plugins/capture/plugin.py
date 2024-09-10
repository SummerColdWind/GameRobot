from plugins.interface import PluginInterface

from plugins.capture.capture import capture, show_image

class Plugin(PluginInterface):
    def __repr__(self):
        return 'A plugin that calls win32API for getting window captures'

    def perform(self, command):
        match command:
            case {'type': 'capture', **rest}:
                """
                Get window capture, and save it.
                If the handle does not exist, no action is performed.

                Args:
                    handle: The name of the handle stored in robot vars, defaults to '__handle'
                    save: Stored in robot vars, defaults to '__capture'
                """
                __save = rest.get('save', '__capture')
                __handle = rest.get('name', '__handle')
                handle = self.robot.vars.get(__handle)
                if handle:
                    image = capture(handle)
                    self.robot.vars[__save] = image
            case {'type': 'show_capture', **rest}:
                """
                Generate a window to show capture.
                
                Args:
                    name: The name of the capture stored in robot vars, defaults to '__capture'
                    wait: Window auto-destruction time (ms). If it is 0, it persists. Defaults to 0
                """
                __capture = rest.get('name', '__capture')
                __wait = rest.get('wait', 0)
                image = self.robot.vars.get(__capture)
                if image is not None:
                    show_image(image, __wait)

            case _:
                raise RuntimeError
