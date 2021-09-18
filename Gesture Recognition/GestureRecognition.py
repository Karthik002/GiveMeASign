import HandTrackingModule as htm

detector = htm.HandDetector(min_detection_confidence=0.85)

# returns 1 for thumbs up, -1 for thumbs down, 0 otherwise
def getThumbsUpDown(img):
    
    # hand recognition algorithms
    img = detector.findHands(img, False)
    lmList = detector.findPosition(img, False)

    # gesture recognition algorithm for thumbs up/down
    return detector.thumbsUpDown(img, False)

# returns rating between 1-5 based on number of fingers up
def getRating(img):
    
    # hand recognition algorithms
    img = detector.findHands(img, False)
    lmList = detector.findPosition(img, False)

    return detector.fingersUp(img, False)
