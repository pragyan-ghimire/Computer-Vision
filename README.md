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

✨ Keep Learning !! ✨


