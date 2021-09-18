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
    img_bytes = request.data[22:]
    img = np.array(Image.open(io.BytesIO(img_bytes)))

    # f = open("img.png", "wb")
    # f.write(base64.b64decode(img[22:]))
    # f.close()
    
    # img = request.data
    # gestureMode = "YesNo"
    # detector = htm.HandDetector(min_detection_confidence=0.85)
    # img = detector.findHands(img, False)
    # lmList = detector.findPosition(img, False)
    # if (gestureMode == "YesNo"):
    #     print(detector.thumbsUpDown(img))
    return jsonify({"something":"something"})
if __name__ == '__main__':
    app.run()