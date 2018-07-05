import cv2
#import numpy
#import matplotlib.pyplot as plot

w = 100
h = 100
color = (0, 255, 0)

x1,y1 = 120,80
x2,y2 = 120,200
x3,y3 = 250,100
x4,y4 = 400,200


cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (500, 350), interpolation=cv2.INTER_CUBIC)
    cv2.rectangle(frame,(x1,y1), (x1+w, y1+h), color)
    cv2.rectangle(frame,(x2,y2), (x2+w, y2+h), color)
    cv2.rectangle(frame,(x3,y3), (x3+w, y3+150), color)
    #cv2.rectangle(frame,(x4,y4), (x4+w, y4+h), color)
    # show a frame
    cv2.imshow("cap", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
