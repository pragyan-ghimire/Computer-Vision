import cv2 as cv

img = cv.imread('../Resources/Photos/cat.jpg')
# img = cv.imread('../Resources/Photos/cat_large.jpg') # large image is difficult to handle
if img is None:
    print("Failed to load image. Check the path.")
else:
    cv.imshow('Cat', img)
cv.waitKey(0) # keyboard binding function (wait for specific time)

# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # to get out of loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()