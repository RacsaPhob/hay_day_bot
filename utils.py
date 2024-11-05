import cv2
import numpy as np
import pyautogui
from time import sleep

error_template = cv2.imread('images/error.png')
close_template = cv2.imread('images/close.png')
continue_template = cv2.imread('images/continue.png')

error_h, error_w = error_template.shape[:2]
close_h, close_w = close_template.shape[:2]
cont_h, cont_w = continue_template.shape[:2]
gui_templates = ['close', 'continue', 'empty_slot', 'publish', 'ready_magazine', 'lower', 'wheat_shop', 'magazine_time',
                 'make_published', 'occupied_slot', 'sold', 'change', 'published_magazine']
class Match:

    def find_matches(self, value: str):
        template = cv2.imread('images/' + value + '.png')

        h, w = template.shape[:2]
        # Получаем скриншот экрана
        screenshot = pyautogui.screenshot()
        threshold = 0.65  # порог совпадения

        # Преобразуем скриншот в формате RGB в формат BGR, который использует OpenCV

        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        if value != 'error':
            error_match = cv2.matchTemplate(frame, error_template, cv2.TM_CCOEFF_NORMED)
            if len(np.where(error_match >= threshold)[0]):
                raise ReferenceError

        if value not in gui_templates:
            close_match = cv2.matchTemplate(frame, close_template, cv2.TM_CCOEFF_NORMED)
            ys, xs = np.where(close_match >= threshold)
            if len(ys):
                pyautogui.click(xs[0] + close_w/2, ys[0] + close_h/2)
                sleep(.5)
                #pyautogui.mouseDown(xs[0] + close_w/2, ys[0] + close_h/2)
                #pyautogui.mouseUp()

        continue_match = cv2.matchTemplate(frame, continue_template, cv2.TM_CCOEFF_NORMED)
        ys, xs = np.where(continue_match >= threshold)
        if len(ys):
            pyautogui.click(950, 950)

        # Применяем метод совпадения шаблона
        result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

        # Находим координаты совпадений
        yloc, xloc = np.where(result >= threshold)
        used_locs = []
        for x, y in zip(xloc, yloc):
            for x1, y1 in used_locs:
                if (abs(x - x1) < 50) and (abs(y - y1) < 50):
                    break

            else:
                used_locs.append([x, y])
                yield (x + w / 2), (y + h / 2)

    def find_match(self, value):
        result = list(self.find_matches(value))


        if (len(result)):

            return list(result)[0]

        else:
            print(value)
            sleep(0.3)
            return self.find_match(value)



