import cv2
import numpy as np
import os

cam=cv2.VideoCapture(0)
detection=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

X=[]
name=input("Enter the name")
count=int(input("Enter the number of count"))

while True:

    revel,image=cam.read()

    if revel:
        faces=detection.detectMultiScale(image)
        faces=sorted(faces,key = lambda face:face[2]*face[3],reverse=True)

        if len(faces)>=1:
            x,y,w,h=faces[0]

            face=image[y:y+h , x:x+w]
            t_face=cv2.resize(face,(100,100))
            grey=cv2.cvtColor(t_face,cv2.COLOR_BGR2GRAY)

            cv2.imshow("my image",grey)

    key=cv2.waitKey(10)

    if key==ord("c"):
        X.append(grey.flatten())
        print("number of count of remaining",count)
        count-=1
        if count==0:
            break

cam.release()
cv2.destroyAllWindows()

X_mod = np.array(X)
y_mod = np.full((len(X), 1), name)

data = np.hstack([y_mod, X_mod])

if os.path.exists("pop.npy"):
    load=np.load("pop.npy")
    data=np.vstack([load,data])

np.save("pop.nyp",data)