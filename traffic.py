import numpy as np
import cv2
import time
import datetime
import threading

time = 0

def fun_timer():
    global time
    time = time + 1
    timer = threading.Timer(1, fun_timer)
    timer.start()

def detection(road, time_road):
    global time
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
        if time >= time_road:
            print "time_road = ", time_road
            print "road = ", road
            time = 0
            cap.release()
            return car_num

def main():
    timer = threading.Timer(1, fun_timer)
    timer.start()
    
    time_road0, time_road1, time_road2, time_road3 = [2, 3, 4, 5]
    while True:
        road0_num = detection(0, time_road0)
        print "road0_num = ", road0_num
        road1_num = detection(1, time_road1)
        print "road1_num = ", road1_num
        road2_num = detection(2, time_road2)
        print "road2_num = ", road2_num
        road3_num = detection(3, time_road3)
        print "road3_num = ", road3_num


if __name__ == "__main__":
    main()

