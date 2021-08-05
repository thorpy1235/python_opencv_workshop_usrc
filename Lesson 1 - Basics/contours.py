import cv2
import numpy as np

img =cv2.imread('../Photos/park.jpg')

cv2.imshow('Park',img)

blank = np.zeros(img.shape,dtype='uint8')

#change to gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# #get blur
# blur=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)

# #get canny
canny=cv2.Canny(img,125,175)
cv2.imshow('canny',canny)

# ret,thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
# cv2.imshow('Thresh',thresh)


contours,hierarchies=cv2.findContours(canny,cv2.RETR_LIST,
cv2.CHAIN_APPROX_SIMPLE)
#takes a structuring element
#contours is a list of contours
#RETR_LIST = returns all contours
#CHAIN_APPROX_NONE = does not provide approximation
#CHAIN_APPROX_SIMPLE = provides a simple approximation

print(f'{len(contours)} contours found')

cv2.drawContours(blank,contours,-1,(0,0,255),1)
cv2.imshow('Contours',blank)

cv2.waitKey(0)