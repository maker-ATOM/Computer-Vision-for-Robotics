import cv2
import sys
import numpy
from stack_img import stackImages

# Read image
img = cv2.imread("../media/nissan.jpg")

# kernel for dilation
kernel = numpy.ones((20,20),numpy.uint8)
# print(kernel)

# Convert to GreyScale
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur Image
imgBlur = cv2.GaussianBlur(img,(11,11),10)

# Edge detection
imgEdge = cv2.Canny(img,100,10)

# Dilation
imgDilate = cv2.dilate(imgBlur,kernel)

# Erosion
imgErode = cv2.erode(imgBlur, kernel)

# Size of Image
print(imgGrey.shape)
# (1280, 960, 3) => third argument is channel of colors

# Resize
imgResize = cv2.resize(img, (500,500))

# Crop
imgCropped = img[111:222,222:333]

# cv2.imshow("Orginal", img)
# cv2.imshow("GreyScale", imgGrey)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Edge Detection", imgEdge)
# cv2.imshow("Dilated", imgDilate)
# cv2.imshow("Eroded", imgErode)
# cv2.imshow("Resized", imgResize)
# cv2.imshow("Cropped", imgCropped)

imgStack = stackImages(0.4,([img, imgGrey, imgBlur],[imgEdge,imgDilate,imgErode]))
cv2.imshow("Result", imgStack)

while True:
    if cv2.waitKey(1) &0xFF == ord('q'):
        break


