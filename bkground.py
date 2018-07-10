import numpy as np
import cv2
import time
import datetime

#摄像头 480*640

cap = cv2.VideoCapture(1)

start_flag = 0
car_num = 0

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorMOG2()

while (1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('fgmask', fgmask)
    image, contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(fgmask, contours, -1, (0, 255, 0), 2)

    minArea = 10000

    for c in contours:

        Area = cv2.contourArea(c)
        if Area < minArea:
            (x, y, w, h) = (0, 0, 0, 0)
            continue
        else:
            (x, y, w, h) = cv2.boundingRect(c)
            #print("x = ", x,"y = ", y)
            if 60<y<160:
                if x >= 430:
                    start_flag = 1
                    print("start 1")
                    time.sleep(0.05)
                elif start_flag==1 and x <= 250:
                    start_flag = 0
                    car_num = car_num + 1
                    print("car_num = ", car_num)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #print("car_num is ", car_num)

    cv2.rectangle(frame, (0, 60), (250, 160), (0, 255, 0), 2)
    cv2.rectangle(frame, (430, 60), (640, 160), (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
#out.release()
cap.release()
cv2.destoryAllWindows()
