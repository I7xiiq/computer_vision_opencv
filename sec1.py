import cv2 as cv

#read photo
img = cv.imread("images.jpeg")

#show photo
cv.imshow('image' , img)

#any bottom in keyboard
cv.waitKey(0)

#close any windows
cv.destroyAllWindows()