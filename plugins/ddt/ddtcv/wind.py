"""
create_time: 2023/2/4 14:01
author: TsangHans
"""
import os
import plugins.ddt.ddtcv as ddtcv
import cv2 as cv
import numpy as np

from plugins.ddt.ddtcv.onnx import ONNXModel

_static_dir = os.path.join(ddtcv.__path__[0], "static")
_default_onnx_model_fp = os.path.join(_static_dir, "model/wind_1_rec_en_number_lite/wind_1_rec_en_number_lite.onnx")
_default_character_dict_fp = os.path.join(_static_dir, "model/wind_1_rec_en_number_lite/wind_dict.txt")
_default_wind_rec_model = ONNXModel(_default_onnx_model_fp, _default_character_dict_fp)
default_x_slice = slice(17, 48)
default_y_slice = slice(461, 537)


def Wind(image: np.ndarray, rec_model: ONNXModel = _default_wind_rec_model, x_slice: slice = default_x_slice,
         y_slice: slice = default_y_slice) -> float:
    x = image[x_slice, y_slice]
    res = rec_model.predict(x)
    direction = wind_direction(image)
    return float(res) * direction


def rec_wind(wind_image: np.ndarray, rec_model: ONNXModel = _default_wind_rec_model) -> float:
    return float(rec_model.predict(wind_image))


def save_wind_image(filename: str, image: np.ndarray, x_slice: slice = default_x_slice,
                    y_slice: slice = default_y_slice) -> None:
    cv.imwrite(filename, image[x_slice, y_slice])

def wind_direction(image: np.ndarray) -> int:
    """
    left is -1 and right is 1
    2024/9/15 10:40
    author: SummerColdWind
    """
    b, g, r = image.item(21, 468, 0), image.item(21, 468, 1), image.item(21, 468, 2)
    direction = 1 if (b == 252 and g == r and g > 240 and r > 240) else -1
    return direction
