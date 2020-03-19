import cv2
import numpy as np

cam=cv2.VideoCapture(0)
cam_1=cv2.VideoCapture("abc.mp4")

theta=np.linspace(0,2000*np.pi,100000)
r=200
x_center=200
y_center=200

X=(r * np.cos(theta) + x_center).astype(int)
Y=(r * np.sin(theta) + y_center).astype(int)

for x,y in zip(X,Y):

    rev_c , image_c= cam.read()
    rev_v ,image_v =cam_1.read()

    if rev_c and rev_v:

        w,h=200,150
        print(x,y,w,h)

        corner=cv2.resize(image_c,(w,h))
        print(corner.shape)

        cut=image_v[y:y+h ,x:x+w]
        cut[:]=corner

        cv2.imshow("circle image",image_v)

    key=cv2.waitKey(100)

    if key==ord("q"):
        break

cam.release()
cam_1.release()
cv2.destroyAllWindows()
