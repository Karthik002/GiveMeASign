from flask import *
from PIL import Image
import io
import numpy as np
import base64
import GestureRecognition as gr

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('webcam.html')

@app.route('/api/v1/classify', methods=['POST'])
def classify():
    img_bytes = base64.b64decode(request.data[22:])
    img = np.array(Image.open(io.BytesIO(img_bytes)))
    
    # result type 1: thumbs up / down
    result = gr.getThumbsUpDown(img)

    # result type 2: rating 1-5
    result = gr.getRating(img)

    return jsonify({"something":result})

if __name__ == '__main__':
    app.run()