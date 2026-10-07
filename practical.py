# ==========================task1========================
# import cv2 as cv
# import sys
# img = cv.imread("images.jpeg")
# if img is None:
#     sys.exit("Could not read the image.")
# cv.imshow("Display window", img)
# k = cv.waitKey(0)
# cv.destroyAllWindows()
# if k == ord("s"):
#     cv.imwrite("./output/saved-starry_night.png", img)


# ==========================task2========================
# import numpy as np
# import cv2 as cv

# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()



# ==========================task3========================
# import numpy as np
# import cv2 as cv

# cap = cv.VideoCapture(0)

# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('./output/output.avi', fourcc, 20.0, (640,  480))

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.flip(frame, 0)
#     out.write(frame)
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break

# cap.release()
# out.release()
# cv.destroyAllWindows()




# ==========================task4========================
# import numpy as np
# import cv2 as cv

# img = np.zeros((512,512,3), np.uint8)

# cv.line(img,(0,0),(511,511),(255,0,0),5)
# cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
# cv.circle(img,(447,63), 63, (0,0,255), -1)
# cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# pts = np.array([[10,5],[100,10],[150,70],[20,100]], np.int32)
# pts = pts.reshape((-1,1,2))
# cv.polylines(img,[pts],True,(0,255,255))

# font = cv.FONT_HERSHEY_SIMPLEX
# cv.putText(img,'Eng. Abdelraouf Hawash',(10,500), font, 1,(255,255,255),2,cv.LINE_AA)

# cv.imshow("Display window", img)
# cv.waitKey(0)
# cv.destroyAllWindows()



# ==========================task5========================
# import cv2 as cv
# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )


# ==========================task6========================