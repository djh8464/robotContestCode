import os.path

import cv2
import sys

num=int(float(sys.argv[1]))
dir=sys.argv[2]+"/"

cap = cv2.VideoCapture(0)
for i in range(1,num):
    ret, frame = cap.read()
    cv2.imwrite("./data/"+dir+str(i)+".jpg",frame)

cap.release()
