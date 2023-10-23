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

# other formats => switching colors (B to R, G to G and R to B)
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Blur Image
imgBlur = cv2.GaussianBlur(img,(11,11),10)
imgBlur = cv2.blur(img, (1,1))
imgBlur = cv2.medianBlur(img, 25)

# Edge detection
imgEdge = cv2.Canny(imgBlur,100,10)

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

# Thresholding
ret, imgThreshold = cv2.threshold(imgGrey, 40, 255,cv2.THRESH_BINARY)
imgAdaptiveThreshold = th3 = cv2.adaptiveThreshold(imgGrey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,12)

# cv2.imshow("Orginal", img)
# cv2.imshow("GreyScale", imgGrey)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Edge Detection", imgEdge)
# cv2.imshow("Dilated", imgDilate)
# cv2.imshow("Eroded", imgErode)
# cv2.imshow("Resized", imgResize)
# cv2.imshow("Cropped", imgCropped)
# cv2.imshow("Thresholding", imgThreshold)

imgStack = stackImages(0.4,([img, imgGrey, imgBlur],[imgEdge,imgDilate,imgErode],[imgThreshold, imgAdaptiveThreshold,imgThreshold]))
cv2.imshow("Result", imgStack)

while True:
    if cv2.waitKey(1) &0xFF == ord('q'):
        break


