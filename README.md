# Fundamentals

Images are just 2D arrays.
<br>Specifically objects of numpy arrays.

Images are made of pixels - individual cells of the array

Terms like VGA, HD, FulHD, 4k defined the size of image in pixels.

Videos are nothing just images flashed multiple time a second.

Binary Image : Image whose cells only have two values typically zero and one.

Usually black is denoted by 0 and white with 255, each image size being 8 bit long. 

Human eyes has three types of photoreceptor cells for color, kind of three types of sensors for perception and each sensor responds to RGB individually. 


# Perception

Birds like gannets determine the time to collision and not distance.

humans have telescopic visual system.

Primary components for cameras.
- Lens
- Imaging chip

Changing the focal length of the lens results in blurring of the image.

# Single View Geometry.

# opencv

**Axis convention:**

```python
(0,0)
   --------→
   |
   |
   |
   ↓
```

**Color Spaces:**
- RGB => Red, Green, Blue
- BGR => Blue, Green, Red
- HSV => Hue, Saturation, Value

<p align="center">
	<img src="images/hsl_hsv.png" width="290" height="290"/>
</p>

**Operations:**
- Convert to greyscale
- Blur : Replace a pixel by the average of neighboring pixels 
- Edge detection : Canny Algorithm
- Dilation : Enlarge regions to make feature more prominent
- Erosion : Reduce features
- Thresholding

**Transformations:**
- Translations
while cap.isOpened(
while cap.isOpened():
    
	ret, img = cap.read()

	h, w, _ = img.shape

	width = 1000
	height = int(width*(h/w))
	img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
 
	corners, ids, rejected = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)

	detected_markers = aruco_display(corners, ids, rejected, img)

	cv2.imshow("Image", detected_markers)):
    
	ret, img = cap.read()

	h, w, _ = img.shape

	width = 1000
	height = int(width*(h/w))
	img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
 
	corners, ids, rejected = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)

	detected_markers = aruco_display(corners, ids, rejected, img)

	cv2.imshow("Image", detected_markers)
- Rotations
- Flip
- Crop
- Resize

**Objects:**
- Generation of Image
- Lines
- Rectangles
- Circles
- Text

**Warp Perspective**

**Stack Images**

**Color Detection**

A good practice to convert RGB mode to HSV as HSV also takes lighting conditions into account.
<br>
Create a mask and filter out the colors using bitwise AND operation not wanted, that simple.

**Contour Detection**

Convert to GrayScale. To simply the process
<br>
Apply Blur if necessary to reduce noise
<br>
Apply edge detection

Or simply use findContours method.

Shapes can also be detected using contours.

Bounding Boxes are added to enclose the contours and display the object.

# Aruco Markers

Type of barcode like markers used for mostly calibration of camera and reference points for tracking and recognizing objects or positions in the real world.

ArUco markers are based on Hamming code.<br>
In the grid, the first, third and fifth columns represent parity bits. The second and fourth columns represent the data bits. Hence, there are ten total data bits.

A predefined dictionary is used for detection and generation of markers.

The dictionaries follow a specific naming convention NxN_M<br>
Where NxN defines the size of the marker in terms of gid cells and also bit size of information it contains so A 5x5 marker hsa 5x5 grd cell and contains 25 bit info, each cell represents a single bit

M represents the total unique markers will be generate.

Each pattern within the dictionary has a unique ID associated.

# Usage

Requirements:

```python
Python version: 3.10.12
Numpy version: 1.21.5
OpenV version: 4.6.0
Numpy path: /home/aditya/.local/lib/python3.10/site-packages/numpy/__init__.py
OpenV path: /home/aditya/.local/lib/python3.10/site-packages/cv2/__init__.py

```

```python
pip3 install opencv-contrib-python==4.6.0.66
```

Clone the repository.

```python
git clone git@github.com:maker-ATOM/Computer-Vision-for-Robotics.git
```

Move to root of directory.
```python
cd <path_to_cloned_directory>/fundamentals
```

Execute the script
```python
python3 read_data.py
```

If in any case
```python
pip3 uninstall opencv-contrib-python
pip3 uninstall opencv-python
sudo apt-get remove python3-numpy
```

Aruco Marker Generation site

```python
https://chev.me/arucogen/
```

# Resources

[Computer Vision Engineer](https://www.youtube.com/watch?v=eDIj5LuIL4A) | 
[Murtaza](https://www.youtube.com/watch?v=WQeoO7MI0Bs) |
[freecodecamp](https://www.youtube.com/watch?v=oXlwWbU8l2o) 