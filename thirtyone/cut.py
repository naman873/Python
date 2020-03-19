import cv2

cap = cv2.VideoCapture(0)

while True:

    revel, image = cap.read()


    if revel:
        #x,y,z,w = 100,200,300,400

        #cut=image[y:y+w , x:x+z]
        #cut[:,:,:2]=0                                  #### BGR -> blue , green , red
        #cut[:,:,:1]=0                                  ####  for some part of screen
        #cut[:,:,1:2]=0



        cut = image[:,:]                               ########    for full screen
        cut[:, :, :1] = 0



        cv2.imshow("my image", image)

    key = cv2.waitKey(100)

    if key == ord("q"):
        break
    if key == ord("a"):
        cv2.imwrite("home.png", image)

cap.release()
cv2.destroyAllWindows()