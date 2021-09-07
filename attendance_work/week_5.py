# -*- coding: utf-8 -*-

import cv2
import numpy as np

collage = cv2.imread('../Photos/collage.png')
pentagon = cv2.imread('../Photos/pentagon.png')

pentagon_edges = cv2.Canny(pentagon, 100, 200)
pentagon_contours, heirarchy = cv2.findContours(pentagon_edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
pentagon_blank = np.zeros(pentagon.shape)
cv2.polylines(pentagon_blank, pentagon_contours, True, (255), 1)
pentagon_moments = cv2.moments(pentagon_contours[1])
pentagon_hu_moments = cv2.HuMoments(pentagon_moments)


cv2.imshow('original',collage)

bilateral = cv2.bilateralFilter(collage, 30, 75, 150)

edges = cv2.Canny(bilateral, 240, 255)
cv2.imshow('canny',edges)

contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

blank_image = np.zeros(collage.shape)

good_contours = []

for contour in contours:
    if cv2.contourArea(contour)>75:
        contour_moments = cv2.moments(contour)
        contour_hu_moments = cv2.HuMoments(contour_moments)
        delta = np.sum(pentagon_hu_moments - contour_hu_moments)
        print(delta)
        if (np.abs(delta)<0.0018): #0.002 is our threshold
            print(np.abs(delta))
            good_contours.append(contour)
            cv2.polylines(blank_image,contour,True,(255),1)


cv2.imshow('pentagons', blank_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)