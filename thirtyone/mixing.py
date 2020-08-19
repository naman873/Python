import cv2

cap=cv2.VideoCapture(0)
cap_1=cv2.VideoCapture("abc.mp4")

while True:

    revel_c, image_c=cap.read()
    revel_im , image_im =cap_1.read()

    if revel_c and revel_im:

        x,y,w,h=100,200,200,200

        corner=cv2.resize(image_c,(w,h))
        print(corner.shape)

        cut=image_im[y:y+h , x:x+w]
        print(cut.shape)

        cut[:]=corner
        cut[:,:,0]=0

        cv2.imshow("my image",image_im)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    if key ==ord("c"):
        cv2.imwrite("proper.png",image_c)

cap.release()
cv2.destroyAllWindows()