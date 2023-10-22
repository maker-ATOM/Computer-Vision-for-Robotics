import cv2
import numpy as np

h = 500
w = 500

img = cv2.imread("../media/nissan.jpg")

# ignore the error thrown by VSCode
points = np.float32([[11, 445], [558, 441], [584, 265],[108, 159]])
origin = np.float32([[0, h], [w, h], [w, 0], [0, 0]])

# Draw polyhedron on Original image for reference
vertices = np.array(points, np.int32)
cv2.polylines(img, [vertices], isClosed=True, color=(0, 255, 0), thickness=3)

matrix = cv2.getPerspectiveTransform(points, origin)
imgWrapped = cv2.warpPerspective(img, matrix, (h,w))

cv2.imshow("Image", img)
cv2.imshow("Wrapped Image", imgWrapped)

while True:
    if cv2.waitKey(1) &0xFF == ord('q'):
        break