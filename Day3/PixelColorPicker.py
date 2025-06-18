import cv2 as cv

img = cv.imread('../Resources/Photos/lady.jpg')

def mouse_click(event, x, y, flags, param):
    img_copy = param.copy()
    # to check if right mouse
    if event == cv.EVENT_RBUTTONDOWN:       
        # In OpenCV, the y-coordinate (row) comes first, then x-coordinate (column).
        color = img_copy[y, x] # y = row, x= column
        font = cv.FONT_HERSHEY_COMPLEX
        text = f"BGR: {color[0]}, {color[1]}, {color[2]}"
        text_pos = (min(x, img.shape[1] - 300), max(y, 20))
        cv.putText(img_copy, text, text_pos, font, 1, (255, 255, 255), 1)
        cv.imshow('Image', img_copy)
        # print(f"Coordinate pressed: {x, y}")
        
if img is None:
    print("Image was not loaded succesfully.")
else:
    cv.imshow('Image', img)
    cv.setMouseCallback('Image', mouse_click, img)
    cv.waitKey(0)
    cv.destroyAllWindows() # close all the opened windows