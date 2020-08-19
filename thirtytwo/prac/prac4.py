import cv2
import os
import numpy as np

cam=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
X=[]
name=input("enter your name")
count=int(input("enter the count"))

while True:

    revel,image=cam.read()

    if revel:
        faces=cascade.detectMultiScale(image)
        faces=sorted(faces , key =lambda face:face[2]*face[3], reverse=True)

        if len(faces)>=1:
            x,y,w,h=faces[0]

            face=image[y:y+h,x:x+w]
            t_face=cv2.resize(face,(100,100))
            gray=cv2.cvtColor(t_face,cv2.COLOR_RGB2GRAY)

            cv2.imshow("my image",gray)

    key=cv2.waitKey(10)

    if key==ord("c"):
        X.append(gray.flatten())
        print("number of count left",count)
        count-=1
        if count==0:
            break


cam.release()
cv2.destroyAllWindows()

X_mod=np.array(X)
y_mod=np.full((len(X),1),name)

data=np.hstack([y_mod,X_mod])

if os.path.exists("pop.npy"):
    load=np.load("pop.npy")
    data=np.vstack([load,data])

np.save("pop.npy",data)

