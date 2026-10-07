import cv2 as cv

img = cv.imread("images.jpeg")
print(img.shape)
img_resized = cv.resize(img ,(500,500) , interpolation=cv.INTER_CUBIC)
print(img_resized.shape)
cv.imshow('img' , img)
cv.imshow('resize' , img_resized)
cv.waitKey(0)
cv.destroyAllWindows