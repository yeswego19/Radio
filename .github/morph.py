import cv2
import numpy as np
import random
import os

# Ищем все фото в корне репозитория
image_files = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

if len(image_files) < 2:
    print("Ошибка: меньше двух фото в корне репозитория")
    exit(1)

print(f"Найдено {len(image_files)} фото")

images = []
for f in image_files:
    img = cv2.imread(f)
    if img is not None:
        img = cv2.resize(img, (1280, 720))
        images.append(img)

print(f"Успешно загружено {len(images)} изображений")

# Создаём 30-секундное видео (20 fps × 30 сек = 600 кадров)
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
        cv2.putText(frame, "Art Radio • Live", (40, 120), cv2.FONT_HERSHEY_DUPLEX, 3.5, (255,255,255), 6)
        out.write(frame)

out.release()
print("output.mp4 успешно создано и готово")
