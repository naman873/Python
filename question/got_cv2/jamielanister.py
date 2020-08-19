import cv2
import numpy as np
cap=cv2.imread("Jamie_Before.jpg")
mustache=cv2.imread("mustache.png")

while True:

    musth = np.array(mustache)
    musth = musth[::4, ::4]
    jamie = np.array(cap)
    #print(musth.size)
    #print(jamie.size)
    cut = jamie[550:-musth.shape[0] - 310, 300:musth.shape[1] + 350]

    gw, gh, gc = musth.shape

    for i in range(0, gw):
        for j in range(0, gh):
            if musth[i, j][gc] != 0:
                cut[i,j] = musth[i, j,:gc]



    cv2.imshow("my",jamie)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break

cap.release()
cv2.destroyWindow()