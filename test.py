import cv2
import numpy as np
import pyautogui

# Загрузите шаблон
template = cv2.imread('options.png')  # Замените 'template.png' на путь к вашему изображению
h, w = template.shape[:2]

while True:
    # Получаем скриншот экрана
    screenshot = pyautogui.screenshot()

    # Преобразуем скриншот в формате RGB в формат BGR, который использует OpenCV
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Применяем метод совпадения шаблона
    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

    # Находим координаты совпадений
    threshold = 0.65  # Установите порог совпадения
    yloc, xloc = np.where(result >= threshold)

    # Рисуем прямоугольники вокруг найденных объектов
    for (x, y) in zip(xloc, yloc):
        print(x, y)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Отображаем результат
    cv2.imshow("Template Matching", frame)

    # Выход из цикла по нажатию 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()