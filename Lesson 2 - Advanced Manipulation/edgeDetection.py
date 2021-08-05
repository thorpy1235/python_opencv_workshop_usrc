import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('Photos/park.jpg')
cv2.imshow('Park',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Laplacian
lap=cv2.Laplacian(gray,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow('Laplacian',lap)

#Sobel
sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0)
sobely=cv2.Sobel(gray,cv2.CV_64F,0,1)

#cv2.imshow('Sobel X',sobelx)
#cv2.imshow('Sobel Y',sobely)

#combining sobel
combineSobel=cv2.bitwise_or(sobelx,sobely)
cv2.imshow('Combined Sobel',combineSobel)

#Canny
canny=cv2.Canny(gray,150,175)
cv2.imshow('Canny',canny)

cv2.waitKey(0)