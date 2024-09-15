import numpy as np
import cv2 as cv
import math


def resize_norm_img(rec_image_shape: tuple, img: np.ndarray, max_wh_ratio: float):
    imgC, imgH, imgW = rec_image_shape

    assert imgC == img.shape[2]
    imgW = int((imgH * max_wh_ratio))

    h, w = img.shape[:2]
    ratio = w / float(h)
    if math.ceil(imgH * ratio) > imgW:
        resized_w = imgW
    else:
        resized_w = int(math.ceil(imgH * ratio))

    resized_image = cv.resize(img, (resized_w, imgH))
    resized_image = resized_image.astype('float32')
    resized_image = resized_image.transpose((2, 0, 1)) / 255
    resized_image -= 0.5
    resized_image /= 0.5
    padding_im = np.zeros((imgC, imgH, imgW), dtype=np.float32)
    padding_im[:, :, 0:resized_w] = resized_image
    return padding_im


def ctc_preprocess(image: np.ndarray, rec_image_shape:tuple):
    imgC, imgH, imgW = rec_image_shape[:3]
    max_wh_ratio = imgW / imgH
    h, w = image.shape[0:2]
    wh_ratio = w * 1.0 / h
    max_wh_ratio = max(max_wh_ratio, wh_ratio)

    norm_img = resize_norm_img(rec_image_shape, image, max_wh_ratio)
    norm_img = norm_img[np.newaxis, :]
    return norm_img


def build_preprocess(algorithm="CTC"):
    if algorithm == "CTC":
        res = ctc_preprocess
    else:
        raise ValueError(f"Unexpected value algorithm={algorithm}.")

    return res