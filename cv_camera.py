import cv2

w = 100
h = 100
color = (0, 255, 0)

x1,y1 = 120,80

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    cv2.rectangle(frame,(x1,y1), (x1+w, y1+h), color)
    cv2.imshow("cap", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
