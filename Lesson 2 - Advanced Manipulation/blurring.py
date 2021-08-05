import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('Photos/park.jpg')
cv2.imshow('Base',img)

""" averaging
define a kernel window 
define the middle window as the average of the surrounding pixels
the bigger the kernel, the greater the blur """

average=cv2.blur(img,(3,3))
cv2.imshow('Average Blur',average)

#Gaussian Blur
#sigmaX is standard deviation in x direction
gauss= cv2.GaussianBlur(img, (3,3),0)
cv2.imshow('Gaussian Blur',gauss)

#Median Blur
#Uses median of pixels in a kernel
median=cv2.medianBlur(img,3)
cv2.imshow('Median Blur',median)

#Bilateral Blur
#Most effective blurring
#Retains the edges in an image
bilateral = cv2.bilateralFilter(img,10,35,25)
cv2.imshow('Bilateral',bilateral)

cv2.waitKey(0)

#kernel
# a window drawn over an image that encompasses the pixels
#within them