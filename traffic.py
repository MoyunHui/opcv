import numpy as np
import cv2
import time
import datetime
import threading
import serial


g_time = 0

def fun_timer():
    global g_time
    g_time = g_time + 1
    timer = threading.Timer(1, fun_timer)
    timer.start()

def detection(road, road_time):
    global g_time
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
        maxArea = 18000
        for c in contours:
            Area = cv2.contourArea(c)
            if Area < minArea:
                (x, y, w, h) = (0, 0, 0, 0)
                continue
            else:
                (x, y, w, h) = cv2.boundingRect(c)
                if 30<y<400:
                    if x >= 400:
                        start_flag = 1
                        time.sleep(0.01)
                    elif start_flag==1 and x <= 250:
                        start_flag = 0
                        car_num = car_num + 1
                        print "road %d " % road, "car_num = ", car_num
        #cv2.imshow('frame', frame)
        #cv2.waitKey(1)

        if g_time >= road_time:
            g_time = 0
            cap.release()
            return car_num

        

def main():

    ser = serial.Serial("/dev/ttyAMA0", 38400)
    timer = threading.Timer(1, fun_timer)
    timer.start()
    
    while True: 
        road0_time, road1_time, road2_time, road3_time = [22, 22, 22, 22]


        print "road 0  ", "  start"
        road0_num = detection(0, road0_time)
        print "road 1  ", "  start"
        road1_num = detection(1, road1_time)
        print "road 2  ", "  start"
        road2_num = detection(2, road2_time)
        print "road 3  ", "  start"
        road3_num = detection(3, road3_time)
        ave0 = 14*road0_num/road0_time
        ave1 = 14*road1_num/road1_time
        ave2 = 14*road2_num/road2_time
        ave3 = 14*road3_num/road3_time
        print "car_num = ", road0_num, road1_num, road2_num, road3_num

        diff = int((ave0+ave1) - (ave2+ave3))
        if abs(diff) >= 1:
            road0_time = road0_time + diff
            road1_time = road1_time + diff
            road2_time = road2_time - diff
            road3_time = road3_time - diff

        diff = int((ave0-ave1))
        if abs(diff) >= 1:
            road0_time = road0_time + diff
            road1_time = road1_time - diff

        diff = int((ave2-ave3))
        if abs(diff) >= 1:
            road2_time = road2_time + diff
            road3_time = road3_time - diff
        print "%d, %d, %d, %d" % (road0_time, road1_time, road2_time, road3_time)
        ser.write("a%db%dc%dd%d" % (road0_time, road1_time, road2_time, road3_time))


if __name__ == "__main__":
    main()

