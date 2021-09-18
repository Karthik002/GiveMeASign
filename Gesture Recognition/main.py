import cv2 as cv
import time
from cv2 import data
import numpy as np
import HandTrackingModule as htm

wCam, hCam = 1280, 720
dataCaptured = False
captureInterval = 3
thumbIndexDistance = 50
upCount = 0
downCount = 0

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
prevTime = 0

detector = htm.HandDetector(min_detection_confidence=0.9)

while True:

    if dataCaptured:
        #time.sleep(captureInterval)
        dataCaptured = False

    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    print("Thumbs Up: " + str(upCount) + ", Thumbs Down: " + str(downCount))

    gesture = detector.thumbsUpDown(img)
    if (gesture != 0):


    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv.imshow("Image", img)

    if cv.waitKey(10) and 0xFF == ord('q'):
        break