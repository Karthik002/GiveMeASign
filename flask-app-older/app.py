from flask import *
from PIL import Image
import cv2 as cv
import io
import numpy as np
import base64
import GestureRecognition as gr

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/typeSelect', methods=['GET'])
def typeSelect():
    return render_template('typeSelect.html')

@app.route('/surveyPicker', methods=['GET'])
def surveyPicker():
    return render_template('surveyPicker.html')

@app.route('/createQuestions', methods=['GET'])
def createQuestions():
    return render_template('createQuestions.html')

@app.route('/api/v1/classify', methods=['POST'])
def classify():
    data_dict = json.loads(request.data)
    img_type = data_dict['img_type']
    img_bytes = base64.b64decode(data_dict['img_bytes'][22:])
    img = np.array(Image.open(io.BytesIO(img_bytes)))
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    result = 'null'
    # result type 1: thumbs up / down
    if (img_type == 'thumbs'):
        result = gr.getThumbsUpDown(img)
    
    # result type 2: rating 1-5
    if (img_type == 'rating'):
        result = gr.getRating(img)

    print(result)

    #if result != 0:
        # send request to stop classification for x seconds

    return jsonify({"classification": result})

@app.route('/api/v1/getSurvey', methods=['POST'])
def getSurvey():

    # we should use survey name and password to access the survey from the db but for now we will just mock the data
    surveyNameInput = request.form.get('surveyName')
    surveyPasswordInput = request.form.get('surveyPassword')
    
    status = False
    surveyJson = {}
    if surveyNameInput == "name" and surveyPasswordInput == "password":   # for now default name and pw is 'name' and 'password'
        status = True 
        surveyJson = {
            "name": "My Survey",
            "type": "thumbs",
            "questions": [
                "How are you today?",
                "Are you enjoying hack the north?"
            ]            
        }

    return render_template('thumbsSurvey.html', args=(status, surveyJson))
    

if __name__ == '__main__':
    app.run()