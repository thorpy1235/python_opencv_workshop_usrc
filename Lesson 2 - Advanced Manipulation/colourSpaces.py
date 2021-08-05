import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('Photos/park.jpg')

#BGR to gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#bgr to hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#BGR to LAB
lab=cv2.cvtColor(img,cv2.COLOR_BGR2Lab)

#BGR to RGB 
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow('RGB',rgb)
cv2.imshow('Park',img)

plt.imshow(rgb)
plt.show()



cv2.waitKey(0)