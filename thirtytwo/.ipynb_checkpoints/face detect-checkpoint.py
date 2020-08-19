import cv2
import numpy as np
import time
import os

value=np.load("faces.npy")
x=value[:,1:].astype(np.uint8)
y=value[:,0]

from sklearn.neighbors import KNeighborsClassifier

model=KNeighborsClassifier()
model.fit(x,y)

cam=cv2.VideoCapture(0)
detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    revel , image=cam.read()

    if revel:
        faces=detect.detectMultiScale(image)
        faces=sorted(faces , key= lambda face: face[2] * face[3] ,reverse=True)

        if len(faces)>=1:
            x,y,w,h=faces[0]

            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,0),10)
            face1=image[y:y+h , x:x+w]
            t_face=cv2.resize(face1,(200,200))

            grey=cv2.cvtColor(t_face, cv2.COLOR_BGR2GRAY)
            text=str(model.predict([grey.flatten()]))[0]
            cv2.putText(image ,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),10)

            cv2.imshow("image",image)


    key=cv2.waitKey(10)

    if key==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()












