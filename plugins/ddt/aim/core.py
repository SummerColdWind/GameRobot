from plugins.window.window import get_pos, get_rect
from plugins.capture.capture import capture
from plugins.ddt.ddtcv import Angle, Wind
from plugins.ddt.ddtank import white_rect, small_map, circle
from plugins.ddt.predict import calForce
from plugins.mouse.mouse import mouse_click
from plugins.keyboard.keyboard import key_press_exact

from collections import deque, Counter
import time
import numpy as np

class AimCore:
    def __init__(self, handle):
        self.handle = handle


    def anchor(self, self_position):
        rect_position = get_pos(self.handle)
        relative_position = (self_position[0] - rect_position[0], self_position[1] - rect_position[1])
        return relative_position

    def read(self):
        image = capture(self.handle)
        angle, wind = Angle(image), Wind(image)
        small = small_map(image)
        box, distance = white_rect(small)

        min_confidence = 0.3
        repeat = 5
        max_try = 50
        circle_record = deque(((0, 0), ), maxlen=repeat)
        center, confidence, try_count = (0, 0), 0, 0
        while (confidence < min_confidence or len(circle_record) < repeat) and try_count < max_try:
            try_count += 1
            image1 = small_map(capture(self.handle))
            time.sleep(.015)
            image2 = small_map(capture(self.handle))
            center = circle(image1, image2)
            if center is not None:
                circle_record.append(center)
            counter = Counter(circle_record)
            center, confidence = counter.most_common(1)[0][0], counter.most_common(1)[0][1] / 10
        return angle, wind, box, distance, center

    def predict(self, self_position):
        mouse_click(self.handle, (1, 1), button='middle')
        time.sleep(.1)
        angle, wind, box, distance, center = self.read()
        print(angle, wind, box, distance, center)
        anchor = self.anchor(self_position)
        target = (
            box[0] + distance * 10 * anchor[0] / 1000,
            box[1] + distance * 6 * anchor[1] / 600
        )
        dx, dy = (target[0] - center[0]) / distance, (target[1] - center[1]) / distance
        force = calForce(angle, wind * (-1 if (dx < 0) else 1), abs(dx), -dy)
        print(force)
        return force

    def shot(self, force):
        key_press_exact(self.handle, 'space', force * 40.5)




