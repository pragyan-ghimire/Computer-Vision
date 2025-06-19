import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/lady.jpg')

cv.imshow('Lady', img)

# def translate(img, x, y):
#     transMat = np.float32([[1, 0, x],
#                            [0,1,y]])
# # First row: [1, 0, x]
# # 1 → This keeps the x (horizontal) scale the same.

# # 0 → This means no shearing between x and y.

# # x → This is the number of pixels you want to move right (if x > 0) or left (if x < 0)

# # Second row: [0, 1, y]
# # 0 → No shearing between x and y.

# # 1 → Keeps the y (vertical) scale the same.

# # y → This is the number of pixels to move down (if y > 0) or up (if y < 0)

#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)

# # -x --> left
# # -y --> up
# # x --> right
# # y --> down

# translated = translate(img, 100, 100)
# cv.imshow('Translated', translated)

# # Rotation 
# def rotate(img, angle, rotPoint = None):
#     (height, width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height //2)
    
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width,height)
#     return cv.warpAffine(img, rotMat, dimensions)


# rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)

# Flipping
# 0 -> vertical
# 1 -> horizontal
# -1 -> vertically and horizontally
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# scaling
# it is resizing that is already discussed

# cropping is also already discussed

cv.waitKey(0)