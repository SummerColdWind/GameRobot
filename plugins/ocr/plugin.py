from plugins.interface import PluginInterface
from plugins.image.plugin import IMAGE_SOURCE_DIR
from plugins.ocr.nopaddleocr import OCR
import os

ocr = OCR(os.path.join(os.path.dirname(__file__), './models'))

class Plugin(PluginInterface):
    def __repr__(self):
        return 'A plugin for OCR using PPOCR V4 model.'

    def perform(self, command):
        match command:
            case {'type': 'ocr', 'image': str(image), 'save': str(save)}:
                if image in self.robot.vars.keys():
                    image = self.robot.vars[image]
                elif isinstance(image, str):
                    image = os.path.join(IMAGE_SOURCE_DIR, image)
                self.robot.vars[save] = ''.join(ocr(image))

            case _:
                raise RuntimeError
