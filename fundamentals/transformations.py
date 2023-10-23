import cv2
import sys
import numpy as np
from stack_img import stackImages

# Read image
img = cv2.imread("../media/nissan.jpg")

# kernel for dilation
kernel = np.ones((20,20),np.uint8)
# print(kernel)

# Translate
transMatrix = np.float32([[1,0, 100],[0,1, 100]])
imgTranslate = cv2.warpAffine(img, transMatrix,(img.shape[1], img.shape[0]))

# Rotation
rotMatrix = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 90,1.0)
imgRotation = cv2.warpAffine(img, rotMatrix,(img.shape[1], img.shape[0]))

# Flip
imgFlip = cv2.flip(img, -1)

imgStack = stackImages(0.4,([img, imgTranslate], [imgRotation,imgFlip]))
cv2.imshow("Result", imgStack)

while True:
    if cv2.waitKey(1) &0xFF == ord('q'):
        break


