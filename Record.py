# -*- coding: utf-8 -*-
 
import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('cap_videos/new.avi', fourcc, 60.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==False:
        break;

    # frame = cv.flip(frame,0)

    out.write(frame)
   
    cv.imshow('Record',frame)

    if cv.waitKey(1) & 0xFF == 27:
        break;

cap.release()
out.release()
cv.destroyAllWindows()
