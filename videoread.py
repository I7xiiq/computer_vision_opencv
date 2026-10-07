import cv2 as cv

capture = cv.VideoCapture('snaptik_7689116689350348084_v3.mp4')

while True:
    isTrue , frame = capture.read()

    if isTrue:
        cv.imshow('video' , frame)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()