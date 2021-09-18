import cv2 as cv
import time
from cv2 import data
import numpy as np
import HandTrackingModule as htm

wCam, hCam = 1280, 720
captureInterval = 3
gestureMode = "YesNo"
upCount = 0
downCount = 0

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
prevTime = 0

detector = htm.HandDetector(min_detection_confidence=0.85)

while True:

    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img, False)
    lmList = detector.findPosition(img, False)

    print("Thumbs Up: " + str(upCount) + ", Thumbs Down: " + str(downCount))

    if (gestureMode == "YesNo"):
        gesture = detector.thumbsUpDown(img)
        if (gesture != 0):
            
            if (gesture == 1):
                cv.putText(img, str("Thumbs up"), (100, 170), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                upCount += 1
            elif (gesture == -1):
                cv.putText(img, str("Thumbs down"), (100, 170), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                downCount += 1
            
            time.sleep(captureInterval)
    
    currTime = time.time()
    fps = 1/(currTime-prevTime)
    prevTime = currTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv.imshow("Image", img)

    if cv.waitKey(10) and 0xFF == ord('q'):
        break