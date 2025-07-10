import cv2 as cv


img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("Image", img)

#BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale", gray)

#BGR to HSV
hsv =cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("Hsv", hsv)

#BGR to L*a*b
lab =cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

#BGR to RGB
rgb =cv.cvtColor(img, cv.COLOR_BGR2RGB) # inversion of colors(compared to BGR) is seen
cv.imshow("rbg", rgb)


# inversion from different color space to BGR is available
# but direct conversion from one color space to another( eg. hsv to rgb, lab to hsv ) is not available 
cv.waitKey()