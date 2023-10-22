import cv2

"""
Image
"""
# img = cv2.imread("../media/nissan.jpg")

# cv2.imshow("output", img)
# cv2.waitKey(1000)


"""
Video
"""
# vid = cv2.VideoCapture("../media/cars.mp4")

# while True:
#     success, img = vid.read()
#     cv2.imshow("video", img)
#     cv2.waitKey(30)

"""
Webcam
"""
cam = cv2.VideoCapture(0)

while True:
    success, img = cam.read()
    cv2.imshow("video", img)
    cv2.waitKey(1)