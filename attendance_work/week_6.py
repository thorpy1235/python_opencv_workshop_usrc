# -*- coding: utf-8 -*-

import cv2
import copy

img1 = cv2.imread('../Faces/usrc_all.png')
img2 = cv2.imread('../Faces/usrc_cropped.png')
frame = cv2.imread('../Faces/imageframe.png')

# convert to greyscale
grey1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grey2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


# store the haar face database to haar_cascade
haar_cascade = cv2.CascadeClassifier('../Lesson 3 -Faces/haar_face.xml')

# detect a face and return the rectangular coordinates of the face
faces_rect1 = haar_cascade.detectMultiScale(grey1, scaleFactor=1.1, minNeighbors=8)
faces_rect2 = haar_cascade.detectMultiScale(grey2, scaleFactor=1.1, minNeighbors=11)
# modify minNeighbors to help filter noise


print(f'Number of faces found = {len(faces_rect1)}')
print(f'Number of faces found = {len(faces_rect2)}')

xF = yF = frame.shape[0]
zF = frame.shape[2]

for i in range(xF):
    if all(frame[i,i,:] == 255):
        frame_width = i
        break


# get coordinates from faces_rect and draw rectangles
# also frame faces and save in framed_faces folder
i = 0
for (x, y, w, h) in faces_rect1:
    framed_face = copy.deepcopy(frame)
    scale = 2
    new_w = int(img1[y:y+h, x:x+w, :].shape[1] * scale)
    new_h = int(img1[y:y+h, x:x+w, :].shape[0] * scale)
    
    framed_face[frame_width:frame_width+new_h, frame_width:frame_width+new_w, :] = \
        cv2.resize(img1[y:y+h, x:x+w, :], (new_w, new_h))
    
    filename = 'framed_face_' + str(i) + '.png'
    path = 'framed_faces/' + filename
    
    cv2.imwrite(path, framed_face)
    
    cv2.rectangle(img1, (x, y), (x+w, y+h), (0,255,0), thickness=2)
    
    i += 1
for (x, y, w, h) in faces_rect2:
    cv2.rectangle(img2, (x, y), (x+w, y+h), (0,255,0), thickness=2)


cv2.imshow('Detected Faces all', img1)
cv2.imshow('Detected Faces cropped', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
