import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

# threshold tries to take and binarize the image
ret, thresh = cv.threshold(gray, 124, 255, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found:")

# contourIdx = -1 => draw all contours
cv.drawContours(blank, contours= contours, contourIdx= -1, color= (0,0,255), thickness= 1)
cv.imshow("Contours drawn", blank)

cv.waitKey()