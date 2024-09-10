from plugins.interface import PluginInterface

from plugins.image.image import templ_match
import os
import cv2

IMAGE_SOURCE_DIR = os.path.join(os.path.dirname(__file__), '../../source/images')
IMAGE_FORMAT = ('.png', '.bmp')
IMAGES = {''.join(name.split('.')[:-1]): cv2.imread(os.path.join(IMAGE_SOURCE_DIR, name))
          for name in os.listdir(IMAGE_SOURCE_DIR)
          if any(name.endswith(s) for s in IMAGE_FORMAT)}

class Plugin(PluginInterface):
    def __repr__(self):
        return 'A plugin for image processing'

    def perform(self, command):
        match command:
            case {'type': 'pixel', 'pos': (x, y), **rest}:
                """
                Gets the RGB value of the pixel for the specified position, and save it.
                
                Args:
                    pos: Coordinates, as (x, y)
                    save: Stored in robot vars, defaults to '__last_pixel'
                    handle: The name of the handle stored in robot vars, defaults to '__handle'
                """
                __save = rest.get('save', '__last_pixel')
                __handle = rest.get('handle', '__handle')
                self.robot.do([
                    {'type': 'capture', 'handle': __handle}
                ])
                pixel = self.robot.vars['__capture'][y, x, ::-1]
                self.robot.vars[__save] = tuple(int(x) for x in pixel)
            case {'type': 'templ', 'image': str(image), **rest}:
                """
                Try the template to match the target image 
                    from a screenshot and save the coordinates of the center point.
                If None is found, the result is None.
                """
                __save = rest.get('save', '__last_templ')
                __handle = rest.get('handle', '__handle')
                image = IMAGES.get(image)
                if image is not None:
                    self.robot.do([
                        {'type': 'capture', 'handle': __handle}
                    ])
                    center = templ_match(self.robot.vars['__capture'], image)
                    self.robot.vars[__save] = center
            case _:
                raise RuntimeError

