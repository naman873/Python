import cv2

cap=cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    retval,image=cap.read()

    if retval:
        faces=classifier.detectMultiScale(image)

        for face in faces:
            x,y,w,h=face

            #cv2.circle(image,center=(x+90,y+90),radius=100,color=(0,0,0),thickness=10)
            cv2.rectangle(image,(x,y),(x+w,y+h),color=(0,0,0),thickness=10)

        cv2.imshow("my image",image)

    key=cv2.waitKey(1)

    if key==ord("q"):
        break
    if key==ord("s"):
        cv2.imwrite("save.png",image)

cap.release()
cv2.destroyAllWindows()
