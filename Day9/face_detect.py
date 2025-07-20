import cv2 as cv

img = cv.imread("../Resources/Photos/group 2.jpg")
cv.imshow("Original Image", img)

# harr cascade does not use color for detection
# it uses edge to detect faces

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

harr_cascade = cv.CascadeClassifier("../Day9/harr_face.xml")

# minNeighbors = 3 means it will only detect faces that have at least 3 neighbors
# faces_rect gives us the coordinates of the detected faces
faces_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
 
print(f"Number of faces detected: {len(faces_rect)}")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2) 
cv.imshow("Detected Faces", img)

cv.waitKey(0)