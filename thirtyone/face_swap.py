import cv2

cam=cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    revel,image=cam.read()

    if revel:

        faces=classifier.detectMultiScale(image)
        faces=sorted(faces , key=lambda face:face[2]*face[3],reverse=True)

        if len(faces)>2:
            x1,y1,w1,h1=faces[0]
            x2,y2,w2,h2=faces[1]

            face1=image[y1:y1+h1 , x1:x1+w1]
            face2=image[y2:y2+h2 , x2:x2+w2]

            t_face1=cv2.resize(face2,(w1,h1))
            t_face2=cv2.resize(face1,(w2,h2))

            face1[:]=t_face1
            face2[:]=t_face2

        cv2.imshow("my image",image)

    key=cv2.waitKey(1)
    if key==ord("q"):
        break
    if key==ord("c"):
        cv2.imwrite("top.png",image)

cam.release()
cv2.destroyAllWindows()

