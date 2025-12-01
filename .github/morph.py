import cv2
import numpy as np
import random
import os
from datetime import datetime

# Ищем все jpg/png в корне
image_files = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
if len(image_files) < 2:
    print("Ошибка: меньше 2 фото")
    exit()

images = []
for f in image_files:
    img = cv2.imread(f)
    if img is not None:
        img = cv2.resize(img, (1280, 720))
        images.append(img)

print(f"Найдено и загружено {len(images)} фото")

# Создаём 30-секундное видео (600 кадров, 20 fps)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1280, 720))

for _ in range(600):
    i1 = random.randint(0, len(images)-1)
    i2 = random.randint(0, len(images)-1)
    while i2 == i1:
        i2 = random.randint(0, len(images)-1)

    for step in range(20):
        alpha = step / 19.0
        frame = cv2.addWeighted(images[i1], 1-alpha, images[i2], alpha, 0)
        cv2.putText(frame, "Art Radio • Live", (50, 100), cv2.FONT_HERSHEY_DUPLEX, 3, (255,255,255), 5)
        out.write(frame)

out.release()
print("Видео output.mp4 успешно создано")
