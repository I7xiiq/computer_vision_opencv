import cv2 as cv

url = "http://10.209.43.174:8080/video"

cap = cv.VideoCapture(url)

if not cap.isOpened():
    print("Cannot open mobile camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv.resize(frame, (800, 450))

    cv.imshow('Mobile Camera', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()