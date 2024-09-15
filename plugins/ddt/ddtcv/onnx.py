"""
create_time: 2023/2/4 14:21
author: TsangHans
"""

import numpy as np

from plugins.ddt.ddtcv.abstract import CVModel
from plugins.ddt.ddtcv.tools.load_model import load_onnx
from plugins.ddt.ddtcv.tools.preprocess import build_preprocess
from plugins.ddt.ddtcv.tools.postprocess import build_postprocess


class ONNXModel(CVModel):
    def __init__(self, onnx_model_fp, character_dict_fp, preprocess_method="CTC"):
        self._preprocess_func = build_preprocess(preprocess_method)
        self._session = load_onnx(onnx_model_fp)
        self._postprocess_func = build_postprocess(character_dict_fp)

    def predict(self, image: np.ndarray):
        d_height, d_width, d_channel = image.shape
        input_image_shape = (d_channel, d_height, d_width)  # 模型的输入维度：通道数 * 高度 * 宽度
        norm_image = self._preprocess_func(image, input_image_shape)  # 进行数据预处理

        # 使用模型对预处理数据进行运算
        input_name = self._session.get_inputs()[0].name
        output = self._session.run([], {input_name: norm_image})

        # 将模型的输出进行后处理，得到识别结果
        res = self._postprocess_func(output)[0][0]
        return res

