import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap1=cv2.VideoCapture("abc.mp4")

theta=np.linspace(0,2000*np.pi,10000)
r=200
x_center=200
y_center=200

X=(r*np.cos(theta) + x_center).astype(int)
Y=(r * np.sin(theta) +y_center).astype(int)

for x,y in zip(X,Y):

    revel_i , image_i=cap.read()
    revel_c ,image_c=cap1.read()

    if revel_i and  revel_c:
        w,h=300,400

        image=cv2.resize(image_i,(w,h))
        cut=image_c[y:y+h,x:x+w]
        cut[:]=image
    
    cv2.imshow("image",image_c)


    key=cv2.waitKey(1)

    if key ==ord("q"):
        break

