import cv2
import numpy as np
import os

from sklearn.neighbors import KNeighborsClassifier

data = np.load("faces.npy")
X = data[:, 1:].astype(np.uint8)
y = data[:, 0]

model = KNeighborsClassifier()
model.fit(X, y)

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:

    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)

        # area ke base pe sort kiya
        faces = sorted(faces, key=lambda face: face[2]*face[3], reverse=True)

        if len(faces) >= 1:
            # sabse bada thooth
            x1, y1, w1, h1 = faces[0]

            cv2.rectangle(image, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 10)

            # face kaat ke nikaal liya
            face1 = image[y1:y1+h1, x1:x1+w1]

            # face is now 100x100x3
            t_face1 = cv2.resize(face1, (100, 100))

            # face is now 100x100
            gray = cv2.cvtColor(t_face1, cv2.COLOR_BGR2GRAY)

            text = str(model.predict([gray.flatten()])[0])

            cv2.putText(image, text, (x1+10, y1-30), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3)

            cv2.imshow("swapped", image)

    key = cv2.waitKey(10)

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()












