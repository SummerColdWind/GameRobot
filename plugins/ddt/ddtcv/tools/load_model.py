import functools

import onnxruntime as ort


@functools.lru_cache(5)
def load_onnx(onnx_model_path):
    return ort.InferenceSession(onnx_model_path, None)
