import numpy as np
import os
import cv2



def templ_match(image, templ, threshold=0.9, multi=False):
    """模板匹配"""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templ = cv2.cvtColor(templ, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(image, templ, cv2.TM_CCOEFF_NORMED)
    w, h = templ.shape[::-1]
    if not multi:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        center = int(max_loc[0] + w / 2), int(max_loc[1] + h / 2)
        return center if max_val >= threshold else None
    else:
        loc = np.where(res >= threshold)
        result = [(int(pt[0] + w / 2), int(pt[1] + h / 2)) for pt in zip(*loc[::-1])]
        return result



