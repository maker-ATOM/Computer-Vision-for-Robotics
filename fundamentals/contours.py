import cv2
import sys
import numpy
from stack_img import stackImages

# kernel for dilation
kernel = numpy.ones((3,3),numpy.uint8)
# print(kernel)

img = cv2.imread("../media/nissan.jpg")
imgContour = img.copy()

# Convert to GrayScale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gaussian Blur to reduce noise
imgBlur = cv2.GaussianBlur(img,(3,3),1)

# Edge detection
imgCanny = cv2.Canny(imgBlur,200,400)

# Dilation
imgDilate = cv2.dilate(imgCanny,kernel)

# using in-build method
# Should perform on the original image instead
contours,_ = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(imgContour, [cnt], -1, (255,255,0),3)
   
imgStack = stackImages(0.4,([img, imgCanny],[imgDilate,imgContour]))
cv2.imshow("Result", imgStack)


while True:
    if cv2.waitKey(1) &0xFF == ord('q'):
        break


