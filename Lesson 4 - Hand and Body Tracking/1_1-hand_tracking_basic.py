import cv2
import mediapipe as mp
import time
import numpy as np




cap = cv2.VideoCapture(0) #use webcam

#black screen
black_screen = np.zeros((512,512,3),dtype='uint8')

#test img


mpHands = mp.solutions.hands
hands  = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
#static_image_mode= False - will sometimes detect or track
#                 = True - will always detect
#max_num_hands

pTime =0 #previous time
cTime =0    #current time

while True:
    success, img = cap.read()

    #resize img
    #img= cv2.resize(img,(512,512))

    #convert to RGB
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    #check if hand has been detected
    if results.multi_hand_landmarks:
        #draw detected hands
        for handLms in results.multi_hand_landmarks:
            #get hand info
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c = black_screen.shape #height, width, channels
                cx, cy = int(lm.x*w), int(lm.y*h) #center width, center height
            
                if id ==0: #first landmark
                    cv2.circle(black_screen, (cx,cy), 5, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(black_screen, handLms,mpHands.HAND_CONNECTIONS)
            #HAND_CONNECTIONS returns the hands with connecting lines

    #determine fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
    (255,0,255),3)
    
    cv2.imshow("Image", img)
    cv2.imshow("Black screen",black_screen)
    black_screen = np.zeros((512,512,3),dtype='uint8')

    cv2.waitKey(1)

