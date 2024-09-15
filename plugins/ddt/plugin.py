from plugins.interface import PluginInterface

from plugins.ddt.ddtcv import Angle, Wind
from plugins.ddt.predict import calForce
from plugins.ddt.aim.ui import AimUI

class Plugin(PluginInterface):
    def __repr__(self):
        return '一个专门用于大陆版本弹弹堂3的插件'

    def perform(self, command):
        match command:
            case {'type': 'ddt.wind', **rest}:
                """ image shape must be (1000, 600) """
                __image = rest.get('image', '__capture')
                __save = rest.get('save', '__ddt.wind')
                if (image := self.robot.vars.get(__image)) is not None:
                    wind = Wind(image)
                    self.robot.vars[__save] = wind
            case {'type': 'ddt.angle', **rest}:
                """ image shape must be (1000, 600) """
                __image = rest.get('image', '__capture')
                __save = rest.get('save', '__ddt.angle')
                if (image := self.robot.vars.get(__image)) is not None:
                    angle = Angle(image)
                    self.robot.vars[__save] = angle
            case {'type': 'ddt.force',
                  'angle': int() | float() as angle,
                  'wind':  int() | float() as wind,
                  'dx':  int() | float() as dx,
                  'dy':  int() | float() as dy,
                  **rest}:
                __save = rest.get('save', '__ddt.force')
                res = calForce(angle, wind, dx, dy)
                self.robot.vars[__save] = res
            case {'type': 'ddt.aim', **rest}:
                __handle = rest.get('handle', '__handle')
                handle = self.robot.vars.get(__handle)
                if handle:
                    AimUI(handle)


        raise RuntimeError



