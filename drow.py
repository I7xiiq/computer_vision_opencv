import cv2 as cv
import numpy as np

empty = np.zeros((600,600,3) , dtype='uint8')
cv.imshow('empty' , empty)

empty[:] = 0,0,255
cv.imshow('colored' , empty)

cv.rectangle(empty, (0,0) , (300,300) , (0,255,255) , thickness=3)
cv.imshow('rectangle' , empty)

cv.waitKey(0)
cv.destroyAllWindows()