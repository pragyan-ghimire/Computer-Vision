# Image Recognition with OpenCV

A beginner‑friendly project skeleton for experimenting with image recognition and computer‑vision techniques using **OpenCV** in Python.

---

## Day 1
### Setting up workspace
- Created Virtual Environment
- Installed Required Packages 
``` bash
    pip install opencv-contrib-python
    pip install caer
```
### Learned about reading image 
- img = cv.imread('filepath') to read image
- cv.imshow('window name', img) to show image

### Learned about reading videos
- capture = cv.VideoCapture('vid_path')
- As video is a series of image played, we ran while loop
    - isTrue, frame = capture.read(), capture.read() returns a bool and frame of image
    - cv.imshow('win_name', frame), to show each frame of video

---

## Day2
### Rescale Image and Videos
- resize() function of cv was explored

### Draw on Image
- Learned to create blank image
- Learned to draw rectangle, circle, line and write text.

---

## Day3

### Pixel Color Picker
- A simple mini project to apply what I learned in Day 1 and Day 2
- Some extra stuff like mouse event was also learned during the process of creation
    - mouse_click(event, x, y, flags, param)
        - event – integer code such as cv2.EVENT_LBUTTONDOWN.
        - x,y - mouse coordinates in the window.
        - flags – bit‑mask of modifier keys/buttons pressed.
        - param – anything you want; defaults to None.
    - cv2.setMouseCallback('Image', mouse_click)

---

## Day4
   Remember Image is just an array of pixels.
### Essential functions of open cv
- Converting image to gray scale: cv.cvtColor(img, cv.COLOR_BGR2GRAY)
- Bluring the image: cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
- Edge cascading: cv.Canny(img, 125, 175)
- Dilating image: cv.dilate(canny, (7,7), iterations= 1)
- Eroding dialted image: cv.erode(dilated, (3,3), iterations= 1)
- Resize image: cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
- Cropping image: cropped = img[50:200, 200:400]

### Transformations
- Translate, Scale, Rotate, crop and flip

---

## Day5
### Contours
- Contour are the curves that connect continuous points along the boundary of an object, surface that shares the same color or intensity.
- The contours of canny edges were not much different
- **cv2.findContours** detect contours in binary images(obtained after edge detection or thresholding)
- **cv2.drawcontours** draws the detected contours on image.

### Color Spaces
- There are various color spaces that are available.
- The default color space for opencv is BGR.( outside opencv RGB is accepted.)
- We can convert from BGR to different color spaces and vice-versa. But the direct conversion from one color space to another( where one of them is not BGR ) is not available.

---

## Day6

### Color Channels
-  We can split a multi-channel image into its individual single-channel components using **cv2.split()** functions and merge single-channel images together to form multi-channel image using **cv2.merge()** function. 

---

## Day7

### Blurring Techniques
They are used for smoothing pictures/images.  The kernel size determines the area of the input that the filter considers at each step. 
Larger kernels can capture more global context and larger patterns, while smaller kernels focus on finer details. 
- **Average Blurring**: Used to reduce image detail and noise by averaging the pixel values within a defined neighborhood.
- **Gausian Blurring**: This method applies a Gaussian filter to the image, which is a weighted average of the pixels.
- **Median Blurring**: This method replaces each pixel's value with the median of its neighbors.
- **Bilateral Blurring**: This method applies a bilateral filter to the image, which is a combination of Gaussian filtering and edge-preserving smoothing.

### Bitwise Operation
- **Bitwise AND :** returns the intersection of the two regions
- **Bitwise OR :** returns the union of the two regions
- **Bitwise XOR :** returns the non-intersection of the two regions
- **Bitwise NOT :** returns inverse of a region

---

## Day8

### Masking
- Image masking in OpenCV involves isolating a specific region of interest within an image

### Histogram
- We can find histogram for grayscale or colourful images.
- Histogram is a plot of no. of pixels vs pixel values.
- It helps to analyze the image (contrast, brightness, intensity distribution etc)

---
✨ Keep Learning !! ✨


