import cv2

for i in range(4):
    print i
    cap = cv2.VideoCapture(i)
    while(1):
        ret, frame = cap.read()
        cv2.rectangle(frame, (0, 30), (250, 400), (0, 255, 0), 2)
        cv2.rectangle(frame, (400, 30), (640, 400), (0, 255, 0), 2)

        cv2.imshow("cap", frame)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break
cap.release()
cv2.destroyAllWindows()
