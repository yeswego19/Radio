Pythonimport cv2
import numpy as np
import random
import os
import time

# Папка с твоими портретами
IMAGE_DIR = "faces"

# Проверяем, есть ли папка
if not os.path.exists(IMAGE_DIR):
    print(f"ОШИБКА: папка {IMAGE_DIR} не найдена! Создай её и положи туда 10 jpg-файлов.")
    exit()

# Загружаем все картинки из папки
image_files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
if len(image_files) < 2:
    print("ОШИБКА: нужно минимум 2 фото в папке faces/")
    exit()

images = []
for f in image_files:
    path = os.path.join(IMAGE_DIR, f)
    img = cv2.imread(path)
    if img is not None:
        img = cv2.resize(img, (640, 640))
        images.append(img)

print(f"Загружено {len(images)} портретов")

# Параметры
DURATION_PER_TRANSITION = 5   # секунд между сменой
FPS = 20
STEPS = DURATION_PER_TRANSITION * FPS

# Основной бесконечный цикл
frame_count = 0
while True:
    # Выбираем две случайные картинки
    idx1 = random.randint(0, len(images)-1)
    idx2 = idx1
    while idx2 == idx1:
        idx2 = random.randint(0, len(images)-1)

    img1 = images[idx1]
    img2 = images[idx2]

    # Плавный морфинг между ними
    for i in range(STEPS + 1):
        alpha = i / STEPS
        morph = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)

        # Надпись
        text = f"Art Radio • {frame_count + 1}"
        cv2.putText(morph, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)

        cv2.imshow("Morph Radio", morph)
        if cv2.waitKey(1) == 27:  # Esc — выход
            cv2.destroyAllWindows()
            exit()

        frame_count += 1

    # Небольшая пауза в конце перехода
    time.sleep(0.1)
