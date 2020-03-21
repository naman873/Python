import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

X = []

name = input("Enter your name : ")
count = int(input("Enter number of samples : "))

while True:

    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)

        # area ke base pe sort kiya
        faces = sorted(faces, key=lambda face: face[2]*face[3], reverse=True)

        if len(faces) >= 1:
            # sabse bada thooth
            x1, y1, w1, h1 = faces[0]

            # face kaat ke nikaal liya
            face1 = image[y1:y1+h1, x1:x1+w1]

            # face is now 100x100x3
            t_face1 = cv2.resize(face1, (100, 100))

            # face is now 100x100
            gray = cv2.cvtColor(t_face1, cv2.COLOR_BGR2GRAY)

            cv2.imshow("swapped", gray)

    key = cv2.waitKey(10)

    if key == ord("c"):

        # Add item to train data
        X.append(gray.flatten())
        count -= 1
        print("Faces remaining", count)
        if count == 0:
            break


cap.release()
cv2.destroyAllWindows()

X_mod = np.array(X)
y_mod = np.full((len(X), 1), name)

data = np.hstack([y_mod, X_mod])

if os.path.exists("faces.npy"):
    old = np.load("faces.npy")
    data = np.vstack([old, data])

np.save("faces.npy", data)