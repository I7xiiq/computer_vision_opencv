import numpy as np
import cv2 as cv

def nothing(x):
    pass

drawing = False

def paint(event, x, y, flags, param):
    global drawing

    r = cv.getTrackbarPos('R', 'Paint')
    g = cv.getTrackbarPos('G', 'Paint')
    b = cv.getTrackbarPos('B', 'Paint')
    radius = max(1, cv.getTrackbarPos('Radius', 'Paint'))
    color = (b, g, r)

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        cv.circle(img, (x, y), radius, color, -1)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img, (x, y), radius, color, -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('Paint')

cv.createTrackbar('R', 'Paint', 255, 255, nothing)
cv.createTrackbar('G', 'Paint', 255, 255, nothing)
cv.createTrackbar('B', 'Paint', 255, 255, nothing)
cv.createTrackbar('Radius', 'Paint', 5, 50, nothing)

cv.setMouseCallback('Paint', paint)

while True:
    cv.imshow('Paint', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('c'):
        img[:] = 0
    elif k == ord('s'):
        cv.imwrite('my_paint.png', img)

cv.destroyAllWindows()