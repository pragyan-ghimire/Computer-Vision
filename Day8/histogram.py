import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("Cat", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# we can compute histograms for grayscale images or colourful images

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Cat", gray)


mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow("Mask", mask)
masked = cv.bitwise_and(gray, gray, mask=mask)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins") # intervals of pixel values (brigntness levels)
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Color histogram
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.xlim([0, 256])
colors = ("b", "g", "r")
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.show()

cv.waitKey(0)