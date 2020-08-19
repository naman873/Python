import cv2

cap = cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    revtal, image = cap.read()


    if revtal:
        faces=classifier.detectMultiScale(image)

        for face in faces:
            x,y,w,h=face
            #cv2.rectangle(image,(x,y),(x+w,y+h),color=(0,255,0),thickness=10)
            cv2.circle(image,center=(x+90,y+90),radius=90,color=(0,255,0),thickness=10)

        cv2.imshow("my image", image)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite("classroom.png", image)

cap.release()
cv2.destroyAllWindows()


