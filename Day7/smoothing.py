import cv2 as cv

img = cv.imread("../Resources/Photos/cats.jpg")
if img is None:
    print("Image not found or path is incorrect")
    exit()
cv.imshow("Cats", img)

# Averaging
# This method replaces each pixel's value with the average of its neighbors.
# where ksize is the size of the kernel
# A larger kernel will result in a more blurred image.
average = cv.blur(img, ksize=(3, 3))
cv.imshow("Average", average)

# Gaussian Blurring
# This method applies a Gaussian filter to the image, which is a weighted average of the pixels
# here sigmaX is the standard deviation in the X direction
# A larger sigmaX will result in a more blurred image.
gaussian = cv.GaussianBlur(img, ksize=(3, 3), sigmaX=0)
cv.imshow("Gaussian", gaussian)

# Median Blurring
# This method replaces each pixel's value with the median of its neighbors.
# more effective for removing salt-and-pepper noise
# ksize must be an odd number because the median needs a center pixel
median = cv.medianBlur(img, ksize=3)
cv.imshow("Median", median)

# Bilateral Filtering
# This method applies a bilateral filter to the image, which is a combination of Gaussian filtering and 
# edge-preserving smoothing.
bilateral = cv.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)