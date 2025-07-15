import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8") 

reactagle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", reactagle)
cv.imshow("Circle", circle)

# Bitwise AND 
# returns the intersection of the two shapes/regions
bitwise_and = cv.bitwise_and(reactagle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# Bitwise OR 
# returns the union of the two shapes
bitwise_or = cv.bitwise_or(reactagle, circle)   
cv.imshow("Bitwise OR", bitwise_or)

# Bitwise XOR
# returns the symmetric difference of the two shapes
bitwise_xor = cv.bitwise_xor(reactagle,circle)
cv.imshow("Bitwise Xor", bitwise_xor)

# Bitwise NOT
# returns the inverse of the shape
bitwise_not_rectangle = cv.bitwise_not(reactagle)
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow("Bitwise NOT Rectangle", bitwise_not_rectangle)
cv.imshow("Bitwise NOT Circle", bitwise_not_circle)

cv.waitKey(0)