import cv2
import sys
import numpy as np
import math

def draw_lines(img, rho, degs):
    a = np.cos(math.radians(degs))
    b = np.sin(math.radians(degs))
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

kernel = np.ones((4,1),np.uint8)

img = cv2.imread("perspective.jpg")

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized_image = cv2.equalizeHist(imgGrey)

ret, imgThreshold = cv2.threshold(equalized_image, 25, 255,cv2.THRESH_BINARY)
imgAdaptiveThreshold = th3 = cv2.adaptiveThreshold(equalized_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)

kernel = np.ones((2,3),np.uint8)
imgErode = cv2.dilate(imgThreshold, kernel)

imgEdge = cv2.Canny(imgErode,10,10)


hough_lines = cv2.HoughLines(imgEdge, 1, np.pi/180, threshold=70)

ranges = [[30, 140], [], []]

req_lines = []

vertical_lines = []

image_with_lines = img.copy()
if hough_lines is not None:
    for line in hough_lines:
        rho, theta = line[0]

        theta = math.degrees(theta)

        if (theta < 30 or theta > 140):
            req_lines.append((rho, theta))
        
        if 30 > theta > 70:
            



vertical_lines.append(min(req_lines, key=lambda x: x[1]))
vertical_lines.append(max(req_lines, key=lambda x: x[1]))

for line in vertical_lines:
    draw_lines(image_with_lines, line[0], line[1])

cv2.imshow("Result", image_with_lines)

while True:
    if cv2.waitKey(1) &0xFF == ord('q'):
        break


