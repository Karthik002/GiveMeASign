import HandTrackingModule as htm
import cv2 as cv

detector = htm.HandDetector(min_detection_confidence=0.7)

# returns 1 for thumbs up, -1 for thumbs down, 0 otherwise
def getThumbsUpDown(img):

    img = detector.findHands(img, False)
    lmList = detector.findPosition(img, False)

    # gesture recognition algorithm for thumbs up/down
    return detector.thumbsUpDown(img)

# returns rating between 1-5 based on number of fingers up
def getRating(img):
    
    # hand recognition algorithms
    img = detector.findHands(img, False)
    lmList = detector.findPosition(img, False)

    return detector.fingersUp(img, False)

def main():
    img = cv.imread(f'images/img.jpg')
    print(getThumbsUpDown(img))

if __name__ == "__main__":
    main()