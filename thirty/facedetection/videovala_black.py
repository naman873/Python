import cv2
import time
cap=cv2.VideoCapture(0)    ### 0 represnt web cam


while True:

    revtal, image = cap.read()

    print(type(image))

    if revtal:
        grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        cv2.imshow("my image" , grey)

    key = cv2.waitKey(1)

    if key==ord("q"):
        break
time.sleep(10)
cap.release()
cv2.destroyAllWindows()