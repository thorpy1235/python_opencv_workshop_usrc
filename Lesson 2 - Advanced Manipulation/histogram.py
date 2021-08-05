import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('Photos/park.jpg')
cv2.imshow('Park',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

mask=cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked=cv2.bitwise_and(gray,gray,mask=mask)

cv2.imshow('Masked',masked)

#Gray histogram
grayHist=cv2.calcHist([gray],[0],masked,[256],[0,256])

plt.figure()
plt.title('Greyscale Hist')
plt.xlabel('Bins')
plt.ylabel('Num of pixels')
plt.plot(grayHist)
plt.xlim([0,256])
plt.show()

#Colour hist
colours=('b','g','r')
for i,col in enumerate(colours):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()

cv2.waitKey(0)