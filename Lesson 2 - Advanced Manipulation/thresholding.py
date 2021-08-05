import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('Photos/park.jpg')
cv2.imshow('Park',img)

#change to gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#simple thresholding
threshold, thresh = cv2.threshold(gray, 150,255,cv2.THRESH_BINARY)
# cv2.THRESH_BINARY = type of thresholding
#if not above threshold, set to 0
cv2.imshow('Simple Threshold',thresh)

#simple inverse
threshold, thresh_inv = cv2.threshold(gray, 150,255,cv2.THRESH_BINARY_INV)
# cv2.THRESH_BINARY = type of thresholding
#if not above threshold, set to 0
cv2.imshow('Simple Inverse Threshold',thresh_inv)

#Adaptive Threshold
adaptive_thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,blockSize=11,C=3)
#blockSize=kernel size
#C= constant
cv2.imshow("Adaptive",adaptive_thresh)

cv2.waitKey(0)