import cv2

cap = cv2.VideoCapture(0)

while True:

    retval, image = cap.read()

    print(type(image))

    if retval:

        cv2.imshow("My capture", image)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break