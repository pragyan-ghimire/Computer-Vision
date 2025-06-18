import cv2 as cv

img = cv.imread('../Resources/Photos/lady.jpg')

# 
def mouse_click(event, x, y, flags, param):
        
    # to check if right mouse
    if event == cv.EVENT_RBUTTONDOWN:       
        # In OpenCV, the y-coordinate (row) comes first, then x-coordinate (column).
        color = img[y, x] # y = row, x= column
        font = cv.FONT_HERSHEY_COMPLEX
        
        cv.putText(img, f"BGR: {color[0]}, {color[1]}, {color[2]}", (x, y),
                    font, 1, 
                    (0, 0, 0),
                    2)
        cv.imshow('Image', img)
        # print(f"Coordinate pressed: {x, y}")
        
if img is None:
    print("Image was not loaded succesfully.")
else:
    cv.imshow('Image', img)

cv.setMouseCallback('Image', mouse_click)

cv.waitKey(0)
cv.destroyAllWindows() # close all the opened windows