import cv2
import numpy as np
import matplotlib.pyplot as plt

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv2.circle(blank.copy(),(200,200),200,255,-1)

cv2.imshow('Rectangle',rectangle)
cv2.imshow('Circle',circle)

#Bitwise AND
bitwiseAND=cv2.bitwise_and(rectangle,circle)
cv2.imshow('Bitwise AND',bitwiseAND)

#Bitwise OR
bitwiseOR=cv2.bitwise_or(rectangle,circle)
cv2.imshow('Bitwise OR',bitwiseOR)

#Bitwise XOR
bitwiseXOR=cv2.bitwise_xor(rectangle,circle)
cv2.imshow('Bitwise XOR',bitwiseXOR)

#Bitwise NOT
bitwiseNOT=np.bitwise_not(circle)
cv2.imshow('Bitwise NOT',bitwiseNOT)



cv2.waitKey(0)