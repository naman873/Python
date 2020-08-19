import cv2

cap=cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    revel,image=cap.read()

    if revel:
        faces=classifier.detectMultiScale(image)
        faces=sorted(faces, key=lambda face:face[2]*face[3],reverse=True)

        if len(faces)>2:
            x,y,w,h=faces[0]
            x1,y1,w1,h1=faces[1]

            face1=image[y:y+h,x:x+w]
            face2=image[y1:y1+h1,x1:x1+w1]

            t_face1=cv2.resize(face2,(w,h))
            t_face2=cv2.resize(face1,(w1,h1))

            face1[:]=t_face1
            face2[:]=t_face2

        cv2.imshow("my image",image)

    key=cv2.waitKey(1)

    if key==ord("q"):
        brek