import cv2
import numpy as np

FrameWidth  = 640
Frameheight = 480
cap= cv2.VideoCapture(0)
cap.set(3,  FrameWidth) #for_setting_width_and_pixel
cap.set(4,  Frameheight) #for_setting_height_nd_pixel
cap.set(10, 150)#for_brightness

def empty (a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",(480,300))
cv2.createTrackbar("hue min","Trackbars",0,179,empty)
cv2.createTrackbar("hue max","Trackbars",179,179,empty)
cv2.createTrackbar("sat min","Trackbars",0,255,empty)
cv2.createTrackbar("sat max","Trackbars",255,255,empty)
cv2.createTrackbar("val min","Trackbars",0,255,empty)
cv2.createTrackbar("val max","Trackbars",255,255,empty)


while True:

    success, img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("hue min","Trackbars")
    h_max=cv2.getTrackbarPos("hue max","Trackbars")
    s_min=cv2.getTrackbarPos("sat min","Trackbars")
    s_max=cv2.getTrackbarPos("sat max","Trackbars")
    v_min=cv2.getTrackbarPos("val min","Trackbars")
    v_max=cv2.getTrackbarPos("val max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower= np.array([h_min,s_min,v_min])
    upper= np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("Video",img)
    
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
