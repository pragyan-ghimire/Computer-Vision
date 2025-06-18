import cv2 as cv

def rescaleFrame( frame, scale = 0.75):
    # images, videos and live videos
    width = int(frame.shape[1] * scale) # 1 represents width
    height = int(frame.shape[0] * scale) # O represents height

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)
    

img = cv.imread('../Resources/Photos/cat_large.jpg') 
if img is None:
    print("Failed to load image. Check the path.")
else:
    resized_img = rescaleFrame(frame= img, scale= 0.2)
    cv.imshow('Cat', resized_img)
    # cv.imshow('Cat', img)
cv.waitKey(0) # keyboard binding function (wait for specific time)


def changeRes(width, height):
    # live video
    capture.set(3, width) # 3 for width
    capture.set(4, height) # 4 for height defined by opencv

capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame= frame)
    # cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)

    # to get out of loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()