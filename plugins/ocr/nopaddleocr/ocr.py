import os
import cv2
import numpy as np

from .predict_system import TextSystem, OCRArgs


class OCR:
    def __init__(self, model_dir):
        self.det_model_dir = os.path.join(model_dir, 'det.onnx')
        self.rec_model_dir = os.path.join(model_dir, 'rec.onnx')
        self.rec_char_dict_path = os.path.join(model_dir, 'ppocr_keys_v1.txt')

        self.engine = TextSystem(OCRArgs(
            det_model_dir=self.det_model_dir,
            rec_model_dir=self.rec_model_dir,
            rec_char_dict_path=self.rec_char_dict_path,
        ))


    def __call__(self, image, text_only=True):
        if isinstance(image, str):
            with open(image, 'rb') as file:
                file_data = file.read()
                image_array = np.frombuffer(file_data, np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        boxes, rec_res = self.engine(image)
        rec_res = (x[0] for x in rec_res)

        if text_only:
            return list(rec_res)

        boxes = ((tuple(pos[0]), tuple(pos[2])) for pos in boxes)
        return list(zip(boxes, rec_res))

