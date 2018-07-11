# -*- coding: utf-8 -*
import serial
import time

ser = serial.Serial("/dev/ttyAMA0", 38400)
def main():
    """
    while True:
        count = ser.inWaiting()
        if count != 0:
            recv = ser.read(count)
            ser.write(recv)
        ser.flushInput()
        time.sleep(0.1)
"""
    while True: 
        ser.write("on")
        time.sleep(0.3)
    
if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        if ser != None:
            ser.close()
