"""
create_time: 2023/2/4 14:03
author: TsangHans
"""
import os
import plugins.ddt.ddtcv as ddtcv
import cv2 as cv
import numpy as np

from plugins.ddt.ddtcv.onnx import ONNXModel

_static_dir = os.path.join(ddtcv.__path__[0], "static")
_default_onnx_model_fp = os.path.join(_static_dir, "model/angle_1_rec_en_number_lite/angle_1_rec_en_number_lite.onnx")
_default_character_dict_fp = os.path.join(_static_dir, "model/angle_1_rec_en_number_lite/angle_dict.txt")
_default_wind_rec_model = ONNXModel(_default_onnx_model_fp, _default_character_dict_fp)
default_x_slice = slice(555, 576)
default_y_slice = slice(29, 73)


def Angle(image: np.ndarray, rec_model: ONNXModel = _default_wind_rec_model, x_slice: slice = default_x_slice,
          y_slice: slice = default_y_slice) -> int:
    x = image[x_slice, y_slice]
    res = rec_angle(x, rec_model)
    return res


def rec_angle(angle_image: np.ndarray, rec_model: ONNXModel = _default_wind_rec_model) -> int:
    return int(rec_model.predict(angle_image))


def save_angle_image(filename: str, image: np.ndarray, x_slice: slice = default_x_slice,
                     y_slice: slice = default_y_slice) -> None:
    cv.imwrite(filename, image[x_slice, y_slice])
