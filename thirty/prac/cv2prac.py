import cv2

cap=cv2.VideoCapture(0)

while True:

    retval,image=cap.read()

    if retval:
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR565)

        cv2.imshow("my image",image)

    key=cv2.waitKey(1)

    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()