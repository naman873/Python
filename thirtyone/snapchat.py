import cv2

cap = cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier("haarcascade_eye.xml")
classifier1=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
glass=cv2.imread("glass.png")

while True:

    revtal, image = cap.read()


    if revtal:
        faces=classifier1.detectMultiScale(image)

        for face in faces:
            x,y,w,h=face
            #eye=cv2.rectangle(image,(x,y),(x+w,y+h),color=(0,255,0),thickness=10)
            cut=image[y:y+h,x:x+w]

            eyes=classifier.detectMultiScale(image)
            for eye in eyes:
                ex , ey , ew ,eh=eye
                glases=cv2.resize(glass,width=ew)

                gw , gh , gc=glases

                for i in range(0,gw): 
                    for j in range(0,gh):
                        if glases[i,j][3] !=0:
                            cut[ey + i,ex+j]=glases[i,j]





        cv2.imshow("my image", image)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite("classroom.png", image)

cap.release()
cv2.destroyAllWindows()



import tensorflow



