import cv2
import sys
import numpy as np
from stack_img import stackImages
import matplotlib.pyplot as plt


img = cv2.imread("../media/nissan.jpg")

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_hist = cv2.calcHist([imgGrey], [0], None, [256], [0,256] )

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# imgStack = stackImages(0.4,([img, imgGrey, imgBlur]))
cv2.imshow("Result", img)


while True:
    if cv2.waitKey(1) &0xFF == ord('q'):
        break


