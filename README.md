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


