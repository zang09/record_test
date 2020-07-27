# -*- coding: utf-8 -*-
 
import cv2 as cv

vidcap = cv.VideoCapture('cap_videos/new.avi')
 
count = 0


while(vidcap.isOpened()):
    ret, image = vidcap.read()

    if ret==False:
        break;
   
    if(int(vidcap.get(1)) % 3 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv.imwrite("../Videos/new/haebum%d.jpg" % count, image)
        print('Saved people%d.jpg' % count)
        count += 1

vidcap.release()


