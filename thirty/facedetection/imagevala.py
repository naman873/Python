import cv2

cap=cv2.VideoCapture("hotair.jpeg")

retval , image =cap.read()

if retval:
    cv2.imshow("my image",image)

key=cv2.waitKey(5000)
