# -*- coding: utf-8 -*-

import cv2
import copy

Wall_E = cv2.imread('best_robot_ever.jpeg')

cv2.imshow('cutie', Wall_E)


# halving the image
scale = 0.5

new_width = int(Wall_E.shape[1] * scale)
new_height = int(Wall_E.shape[0] * scale)

img0 = cv2.resize(Wall_E, (new_width, new_height))

cv2.imshow('resized', img0)

# drawing a shape

img1 = copy.deepcopy(Wall_E)

cv2.circle(img1, (new_width, new_height), 30, (0,0,255), thickness=3)

cv2.imshow('circle', img1)

# greyscale, blur, canny

img2 = copy.deepcopy(Wall_E)

# greyscale = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# cv2.imshow('greyscale', greyscale)
# blur = cv2.GaussianBlur(img2, (11,11), cv2.BORDER_DEFAULT)
# cv2.imshow('blur', blur)
# canny = cv2.Canny(img2, 250, 300)
# cv2.imshow('canny', canny)

img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img2 = cv2.GaussianBlur(img2, (11,11), cv2.BORDER_DEFAULT)
img2 = canny = cv2.Canny(img2, 5, 40)

cv2.imshow('filters', img2)

# rotate 45 degrees

img3 = copy.deepcopy(Wall_E)

rot_point = (new_width, new_height)
rot_matrix = cv2.getRotationMatrix2D(rot_point, 45, 1)
img3 = cv2.warpAffine(img3, rot_matrix, (Wall_E.shape[1], Wall_E.shape[0]))

cv2.imshow('rotated', img3)

# close image on keypress

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)