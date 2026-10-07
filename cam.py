import cv2 as cv

vid = cv.VideoCapture(0)

while True:
    isTrue , frame = vid.read()

    if isTrue:
        cv.imshow('camera' , frame)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

vid.release()
cv.destroyAllWindows()