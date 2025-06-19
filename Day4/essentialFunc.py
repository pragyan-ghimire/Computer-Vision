# essential function in open cv
import cv2 as cv

img = cv.imread('../Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blurring a image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(img, 125, 175) # to reduce no. of edges you can pass blur instead of img
cv.imshow('Canny', canny)

# dilating the image
dilated = cv.dilate(canny, (7,7), iterations= 1)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations= 1)
cv.imshow('Eroded', eroded) # got back same edge cascade

# Resize

# Inter_area for scaling down and Inter_linear or cubic for scaling up
resized = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)