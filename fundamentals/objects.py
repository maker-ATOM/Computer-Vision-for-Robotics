import cv2
import numpy as np

# Generation of image
img = np.zeros((500,500,3),np.uint8)

# Lines
cv2.line(img,(10,10), (200,200), (127,127,0), 3)

# Rectangles
cv2.rectangle(img,(50,50),(400,400),(127,0,127),4)

# Circles
cv2.circle(img,(250,250),100,(0,127,127),3)

# Text
cv2.putText(img,"ADITYA",(400,400),cv2.FONT_HERSHEY_COMPLEX,1.0,(255,255,255),1)


cv2.imshow("image", img)

while True:
    if cv2.waitKey(1) &0xFF == ord('q'):
        break