import numpy as np
import cv2
import time
import datetime
import threading

global timer
global proc


def fun_timer(go_ms):
    print 'hello'
    proc = 0

    timer = threading.Timer(go_ms, fun_timer)
    timer.start()

   

def detection(road):
    car_num = 0
    start_flag = 0
    cap = cv2.VideoCapture(road)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgbg = cv2.createBackgroundSubtractorMOG2()
    while (1):
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
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
                if 60<y<160:
                    if x >= 430:
                        start_flag = 1
                        print "start 1"
                        time.sleep(0.05)
                    elif start_flag==1 and x <= 250:
                        start_flag = 0
                        car_num = car_num + 1
                        print "car_num = ", car_num
        if ch_flag == 1:
            cap.release()
            return car_num

def main():
    fun_timer(20)
    while True:
        road0_num = detection(0)
        road1_num = detection(1)
        road2_num = detection(2)
        road3_num = detection(3)


if __name__ == "__main__":
    main()

