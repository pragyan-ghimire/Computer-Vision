# thresholding is a binarization technique
# it converts an image into a binary image (black and white)
# we take some threshold value and convert all pixels above that value to white (255) and all pixels below that value to black (0)

import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# thresh -> binary image
# threshold -> the value we used to binarize the image(150 in this case)
cv.imshow("Simple Thresholding", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholding Inverse", thresh_inv)

# adaptive thresholding
# blockSize must be odd and greater than 1 because it defines the size of the neighborhood area
# C is a constant subtracted from the mean or weighted mean
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blockSize=7, C=5)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)