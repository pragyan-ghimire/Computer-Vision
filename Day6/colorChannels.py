import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/park.jpg")


if img is None:
    print("Image not found or path is incorrect")
    exit()

cv.imshow("Boston",img)

# Create a blank image with the same height and width as the original image
blank = np.zeros(img.shape[:2], dtype="uint8")

b,g,r = cv.split(img)

# to see actual color channel
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

# # Grayscale
# # the spaces with white color has specific intensity for that particular color
# cv.imshow("Blue", b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging different channels

merged = cv.merge([b,g,r])
cv.imshow("Merged Image", merged)

cv.waitKey(0)