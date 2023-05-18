import cv2
import numpy as np
import os
import shutil

PATH = 'Aug'
os.mkdir(PATH)

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.jpg'):
        image = cv2.imread(filename)
        original = image
        height, width = image.shape[:2]

        rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), np.random.randint(30), 0.5)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
        cv2.imwrite(os.path.join(PATH, filename[:-5] + '1.jpg'), rotated_image)

        image = original
        bright = np.ones(image.shape, dtype='uint8') * 50
        bright_image = cv2.add(image, bright)
        cv2.imwrite(os.path.join(PATH, filename[:-5] + '2.jpg'), bright_image)

        image = original
        unbright_image = cv2.subtract(image, bright)
        cv2.imwrite(os.path.join(PATH, filename[:-5] + '3.jpg'), unbright_image)

        image = original
        flip = cv2.flip(image, 3)
        cv2.imwrite(os.path.join(PATH, filename[:-5] + '4.jpg'), flip)

        
for filename in os.listdir(PATH):
    if filename.endswith('.jpg'):
        shutil.move(os.path.join(PATH, filename), os.getcwd())

os.rmdir(PATH)  
        