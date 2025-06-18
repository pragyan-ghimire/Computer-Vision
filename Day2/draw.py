import cv2 as cv
import numpy as np

# There are two ways to draw on image
# Draw on standalone image or blank one

blank = np.zeros((500,500,3), dtype='uint8') # 3 is number of color channel
# cv.imshow("Blank image", blank)

# img = cv.imread('../Resources/Photos/cat.jpg')
# cv.imshow('Image', img)

# 1. Paint the image a certain colour
# blank[:] = 255,0,0  # b, g, r

# making a square
blank[200: 300, 300:400] = 255,0,0

# draw rectangle
cv.rectangle(img= blank, pt1= (0,0),pt2= (250, 250),color= (0,250,0), thickness= 2)

# draw circle
cv.circle(img= blank,center= (250,250),radius= 40, color= (0,255,0),thickness= cv.FILLED)

# draw line
cv.line(img= blank, pt1= (10,10), pt2= (blank.shape[1]//2, blank.shape[0]//2), color= (0,0,255), thickness= 2)

# write text on image
cv.putText(img= blank, text= 'Fire God', org= (250, 250), fontFace= cv.FONT_HERSHEY_COMPLEX, fontScale= 1.0, color= (255,255, 255))

cv.imshow('Shapes', blank)

cv.waitKey(0)

