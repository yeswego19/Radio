import cv2
import numpy as np
import random
import os

# Ищем все jpg/png в корне репозитория
image_files = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
if len(image_files) < 2:
    print("Ошибка: нужно хотя бы 2 фото в корне")
    exit()

images = []
for f in image_files:
    img = cv2.imread(f)
    if img is not None:
        img = cv2.resize(img, (640, 640))
        images.append(img)

print(f"Загружено {len(images)} фото")

while True:
    i1 = random.randint(0, len(images)-1)
    i2 = random.randint(0, len(images)-1)
    while i2 == i1:
        i2 = random.randint(0, len(images)-1)

    img1 = images[i1]
    img2 = images[i2]

    for step in range(50):
        alpha = step / 49.0
        morph = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
        cv2.putText(morph, "Art Radio", (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 4)
        cv2.imshow("Morph", morph)
        if cv2.waitKey(100) == 27:  # Esc
            exit()
