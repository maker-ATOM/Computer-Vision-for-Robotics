#! /usr/bin/env python3


import cv2
import cv2.aruco as aruco
import numpy as np


# Create an empty image for the marker
markerImage = np.zeros((200, 200), dtype=np.uint8)

# Define the ArUco dictionary and generate the marker
dictionary = aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
cv2.aruco.drawMarker(dictionary, 23, 200, markerImage)

# Save the generated marker image to a file
cv2.imshow("output", markerImage)
cv2.waitKey(0)


# img = cv2.imread("../media/aruco.jpg")

# cv2.imshow("output", img)


# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# aruco_dict = aruco.Dictionary(aruco.DICT_4X4_250,4)
# Parameters = aruco.DetectorParameters()
# corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=Parameters)
# print(corners, id)


# cv2.waitKey(2000)



# corners, ids = self.detect_aruco(cv_image)
# print( "image corner generated")

# image = aruco.drawDetectedMarkers(self.gray, corners, ids, borderColor=(0, 255, 0))
# print("drawing")
# cv2.imshow("aruco_tags", image)
# cv2.waitKey(3)