import numpy as np
import cv2
import time

from collections import deque, Counter
from math import dist
from itertools import product


def _small_map(image):
    try:
        return np.argwhere(np.all(image[1, 750:] == [160, 160, 160], axis=-1))[0, 0] + 742
    except IndexError:
        return 700

def small_map(image):
    left = _small_map(image)
    return image[24:120, left:998]

def white_rect(small):
    try:
        img = np.where(np.any(small != [153, 153, 153], axis=-1), 0, 255).astype('uint8')
    except IndexError:
        return None
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((9, 9), 'uint8'))
    contours = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    rectangles = [cv2.boundingRect(cnt) for cnt in contours]
    rectangles = [rect for rect in rectangles if rect[2] > 30]
    if rectangles:
        rect = rectangles[0]
        return (rect[0], rect[1]), rect[2] / 10
    else:
        return None


def circle(image1, image2):
    gray1, gray2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY), cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    intersection = np.where(gray1 == gray2, 0, 255).astype('uint8')
    contours = cv2.findContours(intersection, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if (15 < w < 20 or 15 < h < 20) and abs(w - h) < 3:
            m = cv2.moments(contour)
            cx = int(m['m10'] / m['m00'])
            cy = int(m['m01'] / m['m00'])
            return cx, cy
    else:
        return None





