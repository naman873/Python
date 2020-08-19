import cv2

cap=cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    revel,image =cap.read()

    if revel:

        faceses=classifier.detectMultiScale(image)

        for face in faceses:
            print(face)

            x,y,w,h=face
            #cv2.rectangle(image,(x,y),(x+w,y+h),color=(0,0,0),thickness=10)
            cv2.circle(image,center=(x+90,y+90),radius=100,color=(0,0,0),thickness=10)
        cv2.imshow("image",image)

    key=cv2.waitKey(1)
    if key==ord("q"):
        break

    if key==ord("c"):
        cv2.imwrite("hercascade",image)

cap.release()
cv2.destroyAllWindows()