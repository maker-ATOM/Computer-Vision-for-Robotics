import cv2
import numpy as np

# Initialize the camera or video capture (0 for the default camera)
cap = cv2.VideoCapture(0)

# Create an ArUco dictionary (e.g., DICT_6X6_250)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Create a parameters object
parameters = cv2.aruco.DetectorParameters_create()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect ArUco markers in the frame
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        for i in range(len(ids)):
            # Draw a bounding box around the detected marker
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

    # Display the frame with ArUco marker detection
    cv2.imshow('ArUco Marker Detection', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
