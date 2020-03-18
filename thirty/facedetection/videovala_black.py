import cv2

cap=cv2.VideoCapture(0)


while True:

    revtal, image = cap.read()

    print(type(image))

    if revtal:
        grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        cv2.imshow("my image" , grey)

    key = cv2.waitKey(1)

    if key==ord("q"):
        break