import numpy as np
import cv2
import os
from sklearn.neighbors import KNeighborsClassifier

cap=cv2.VideoCapture(0)

data=np.load("pop.npy")
X=data[:,1:]
y=data[:,0]

model=KNeighborsClassifier()
model.fit(X,y)

classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    revel,image=cap.read()

    if revel:

        faces=classifier.detectMultiScale(image)
        faces=sorted(faces ,key = lambda face:face[2]*face[3],reverse=True)

        if len(faces)>=1:
            x,y,w,h=faces[0]

            cv2.rectangle(image,(x,y),(x+w,y+h),color=(0,0,0),thickness=10)
            face=image[y:y+h,x:x+w]

            t_face=cv2.resize(face,(100,100))
            gray=cv2.cvtColor(t_face,cv2.COLOR_RGB2GRAY)

            text=str(model.predict([gray.flatten()])[0])

            cv2.putText(image,text,(x+10,y-30),cv2.FONT_HERSHEY_COMPLEX,2 ,(155,5,10),3)
            cv2.imshow("image",image)

    key=cv2.waitKey(1)

    if key==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()