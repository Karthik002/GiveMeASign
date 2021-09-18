from flask import *
from PIL import Image
import cv2
import io
import numpy as np
import base64
import HandTrackingModule as htm

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('webcam.html')

@app.route('/api/v1/classify', methods=['POST'])
def classify():
    img_bytes = base64.b64decode(request.data[22:])
    img = np.array(Image.open(io.BytesIO(img_bytes)))
    
    gestureMode = "YesNo"
    detector = htm.HandDetector(min_detection_confidence=0.85)
    img = detector.findHands(img, False)
    lmList = detector.findPosition(img, False)
    result = 0
    if (gestureMode == "YesNo"):
        result = detector.thumbsUpDown(img)
    return jsonify({"something":result})
if __name__ == '__main__':
    app.run()