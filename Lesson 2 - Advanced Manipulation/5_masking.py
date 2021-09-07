import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('..\Photos/park.jpg')
cv2.imshow('Park',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('Blank Image',blank)

mask=cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv2.imshow('Mask',mask)

masked=cv2.bitwise_and(img,img,mask=mask) 
#bitwise AND: if both values 1, result is 1
cv2.imshow('Masked Image',masked)

cv2.waitKey(0)