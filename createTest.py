import os
import cv2
import time

vid = cv2.VideoCapture(0)

if not os.path.isdir("dataset"):
    os.mkdir("dataset")

if not os.path.isdir("dataset/test"):
    os.mkdir("dataset/test")

i = len(os.listdir("dataset/test"))
while(True):
    _, frame = vid.read()
  
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imwrite(f'dataset/test/img{i}.jpg', frame)
    i+=1

    time.sleep(0.1)

vid.release()
cv2.destroyAllWindows()