# Fundamentals

Images are just 2D arrays.
<br>Specifically objects of numpy arrays

Terms like VGA, HD, FulHD, 4k defined the size of image in pixels.

Videos are nothing just images flashed multiple time a second.

Binary Image : Image whose cells only have two values typically zero and one.

Usually black is denoted by 0 and white with 255, each image size being 8 bit long. 


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

**Color Models:**
- RGB => Red, Green, Blue
- HSV => Hue, Saturation, Value

**Transformations:**
- Convert to greyscale
- Blur
- Edge detection : Canny Algorithm
- Dilation : Enlarge regions to make feature more prominent
- Erosion : Reduce features
- Resize
- Crop

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

# Usage

Requirements:

```python
Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0]
Numpy version: 1.26.1
Opencv version: 4.8.1
```

```python

pip install opencv-python
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
# Resources

[Computer Vision Engineer](https://www.youtube.com/watch?v=eDIj5LuIL4A)
[Murtaza](https://www.youtube.com/watch?v=WQeoO7MI0Bs)
[freecodecamp](https://www.youtube.com/watch?v=oXlwWbU8l2o)