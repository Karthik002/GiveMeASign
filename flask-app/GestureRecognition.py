import HandTrackingModule as htm

gestureMode = "YesNo"
detector = htm.HandDetector(min_detection_confidence=0.85)

def getHandGesture(img):
    
    # hand recognition algorithms
    img = detector.findHands(img, False)
    lmList = detector.findPosition(img, False)

    # gesture recognition algorithm for thumbs up/down
    # returns 1 for thumbs up, -1 for thumbs down, 0 otherwise
    if (gestureMode == "YesNo"):
        return detector.thumbsUpDown(img)
