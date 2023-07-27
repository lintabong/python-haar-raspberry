
import cv2
import numpy

cap         = cv2.VideoCapture('dataset_sample/traffic.mp4')
car_cascade = cv2.CascadeClassifier('dataset_sample/classifier/cascade.xml')

while True:
    ret, img = cap.read()

    gray     = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars     = car_cascade.detectMultiScale(gray, 1.5, 2)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

    scale_percent = 60
    width         = int(img.shape[1] * scale_percent / 100)
    height        = int(img.shape[0] * scale_percent / 100)
    dim           = (width, height)
    resized       = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    cv2.imshow('img', resized)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
