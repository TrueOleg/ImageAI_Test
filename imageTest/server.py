# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify, send_file, make_response
import pickle
from flask_cors import CORS
import base64
from PIL import Image
from io import BytesIO
import re, time, base64
from imageai.Detection import ObjectDetection
import os
import json
execution_path = os.getcwd()

app = Flask(__name__)
CORS(app)
# Load the model
# model = pickle.load(open('model.pkl','rb'))
def getI420FromBase64(codec, image_path=""):
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    t = time.time()
    img.save('1' + '.jpg', "JPEG")
    
@app.route('/api/image',methods=['POST'])
def predict():
    
    data = request.get_json(force=True)
    
    getI420FromBase64(data.get('data'))
    # imgdata = data.get('data').decode("base64")
    # filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    # with open(filename, 'wb') as f:
    #   f.write(imgdata)
    detector = ObjectDetection() 
    detector.setModelTypeAsYOLOv3() 
    detector.setModelPath( os.path.join(execution_path , "yolo.h5")) 
    detector.loadModel() 
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "1.jpg"), output_image_path=os.path.join(execution_path , "2.jpg"), minimum_percentage_probability=30)
    print('detection', detections)
    
    response = make_response(send_file('2.jpg', mimetype='image/jpg'))
    response.headers['detection'] = str(detections)
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)
