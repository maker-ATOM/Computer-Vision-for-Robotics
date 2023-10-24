import numpy
import cv2
import sys

print(f"Python version: {sys.version}")
print(f"Numpy version: {numpy.__version__}")
print(f"OpenV version: {cv2.__version__}")

print(f"Numpy path: {numpy.__file__}")
print(f"OpenV path: {cv2.__file__}")



"""
Image
"""
img = cv2.imread("../media/nissan.jpg")

cv2.imshow("output", img)
cv2.waitKey(1000)


"""
Video
"""
# vid = cv2.VideoCapture("../media/cars.mp4")

# while True:
#     success, img = vid.read()
#     cv2.imshow("video", img)
#     cv2.waitKey(30)

# vid.release()
# cv2.destroyAllWindows()

"""
Webcam
"""
# cam = cv2.VideoCapture(0)

# while True:
#     success, img = cam.read()
#     cv2.imshow("video", img)
#     # more the wait more laggy the feed br
#     cv2.waitKey(200)

# vid.release()
# cv2.destroyAllWindows()