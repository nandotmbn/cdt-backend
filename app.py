from flask import Flask, request
from flask_cors import CORS
import numpy as np
import cv2
import tensorflow as tf
from datetime import datetime
import time

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

loaded_model_1 = tf.keras.models.load_model("cdt_model_2")

class_names = ['Demensia Berat', 'Demensia Ringan', 'Demensia Sedang',
               'Tidak Demensia']

@app.post("/")
def upload_file():
    if request.method == 'POST':
        img_to_detect = cv2.imdecode(np.fromstring(
            request.files['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        img_height = img_to_detect.shape[0]
        img_width = img_to_detect.shape[1]
        img_to_detect = cv2.circle(img_to_detect, (int(img_height/2), int(img_width/2)), int(img_width/2), (0,0,0), 2)
        img_to_detect = cv2.resize(
            img_to_detect, (224, 224), interpolation=cv2.INTER_LINEAR)

        # Resize the image (to the same size our model was trained on)
        img = tf.image.resize(img_to_detect, size=[224, 224])

        cv2.imwrite("img/ToDetect.jpg", img_to_detect)

        # Rescale the image (get all values between 0 and 1)
        img = img/255.

        pred = loaded_model_1.predict(tf.expand_dims(img, axis=0))

        # Get the predicted class
        if len(pred[0]) > 1:  # check for multi-class
            # if more than one output, take the max
            pred_class = class_names[pred.argmax()]
        else:
            # if only one output, round
            pred_class = class_names[int(tf.round(pred)[0][0])]

        return pred_class

@app.post("/manual")
def upload_file_manual():
    if request.method == 'POST':
        img_to_detect = cv2.imdecode(np.fromstring(
            request.files['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        img_height = img_to_detect.shape[0]
        img_width = img_to_detect.shape[1]
        img_to_detect = cv2.circle(img_to_detect, (int(img_height/2), int(img_width/2)), int(img_width/2), (0,0,0), 2)
        img_to_detect = cv2.resize(
            img_to_detect, (224, 224), interpolation=cv2.INTER_LINEAR)

        # Resize the image (to the same size our model was trained on)
        img = tf.image.resize(img_to_detect, size=[224, 224])

        # Rescale the image (get all values between 0 and 1)
        img = img/255.

        pred = loaded_model_1.predict(tf.expand_dims(img, axis=0))

        # Get the predicted class
        if len(pred[0]) > 1:  # check for multi-class
            # if more than one output, take the max
            pred_class = class_names[pred.argmax()]
        else:
            # if only one output, round
            pred_class = class_names[int(tf.round(pred)[0][0])]

        return pred_class

@app.post("/create/no")
def create_no():
    if request.method == 'POST':
        img_to_detect = cv2.imdecode(np.fromstring(
            request.files['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        img_height = img_to_detect.shape[0]
        img_width = img_to_detect.shape[1]
        img_to_detect = cv2.circle(img_to_detect, (int(img_height/2), int(img_width/2)), int(img_width/2), (0,0,0), 2)
        img_to_detect = cv2.resize(
            img_to_detect, (224, 224), interpolation=cv2.INTER_LINEAR)

        # Resize the image (to the same size our model was trained on)
        img = tf.image.resize(img_to_detect, size=[224, 224])

        cv2.imwrite(f"newdataset/tidak_demensia/{str(int(time.time()))}.jpg", img_to_detect)

        # Rescale the image (get all values between 0 and 1)
        img = img/255.

        pred = loaded_model_1.predict(tf.expand_dims(img, axis=0))

        # Get the predicted class
        if len(pred[0]) > 1:  # check for multi-class
            # if more than one output, take the max
            pred_class = class_names[pred.argmax()]
        else:
            # if only one output, round
            pred_class = class_names[int(tf.round(pred)[0][0])]

        return pred_class

@app.post("/create/low")
def create_low():
    if request.method == 'POST':
        img_to_detect = cv2.imdecode(np.fromstring(
            request.files['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        img_height = img_to_detect.shape[0]
        img_width = img_to_detect.shape[1]
        img_to_detect = cv2.circle(img_to_detect, (int(img_height/2), int(img_width/2)), int(img_width/2), (0,0,0), 2)
        img_to_detect = cv2.resize(
            img_to_detect, (224, 224), interpolation=cv2.INTER_LINEAR)

        # Resize the image (to the same size our model was trained on)
        img = tf.image.resize(img_to_detect, size=[224, 224])

        cv2.imwrite(f"newdataset/demensia_ringan/{str(int(time.time()))}.jpg", img_to_detect)

        # Rescale the image (get all values between 0 and 1)
        img = img/255.

        pred = loaded_model_1.predict(tf.expand_dims(img, axis=0))

        # Get the predicted class
        if len(pred[0]) > 1:  # check for multi-class
            # if more than one output, take the max
            pred_class = class_names[pred.argmax()]
        else:
            # if only one output, round
            pred_class = class_names[int(tf.round(pred)[0][0])]

        return pred_class

@app.post("/create/medium")
def create_medium():
    if request.method == 'POST':
        img_to_detect = cv2.imdecode(np.fromstring(
            request.files['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        img_height = img_to_detect.shape[0]
        img_width = img_to_detect.shape[1]
        img_to_detect = cv2.circle(img_to_detect, (int(img_height/2), int(img_width/2)), int(img_width/2), (0,0,0), 2)
        img_to_detect = cv2.resize(
            img_to_detect, (224, 224), interpolation=cv2.INTER_LINEAR)

        # Resize the image (to the same size our model was trained on)
        img = tf.image.resize(img_to_detect, size=[224, 224])

        cv2.imwrite(f"newdataset/demensia_sedang/{str(int(time.time()))}.jpg", img_to_detect)

        # Rescale the image (get all values between 0 and 1)
        img = img/255.

        pred = loaded_model_1.predict(tf.expand_dims(img, axis=0))

        # Get the predicted class
        if len(pred[0]) > 1:  # check for multi-class
            # if more than one output, take the max
            pred_class = class_names[pred.argmax()]
        else:
            # if only one output, round
            pred_class = class_names[int(tf.round(pred)[0][0])]

        return pred_class

@app.post("/create/high")
def create_high():
    if request.method == 'POST':
        img_to_detect = cv2.imdecode(np.fromstring(
            request.files['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        img_height = img_to_detect.shape[0]
        img_width = img_to_detect.shape[1]
        img_to_detect = cv2.circle(img_to_detect, (int(img_height/2), int(img_width/2)), int(img_width/2), (0,0,0), 2)
        img_to_detect = cv2.resize(
            img_to_detect, (224, 224), interpolation=cv2.INTER_LINEAR)

        # Resize the image (to the same size our model was trained on)
        img = tf.image.resize(img_to_detect, size=[224, 224])

        cv2.imwrite(f"newdataset/demensia_berat/{str(int(time.time()))}.jpg", img_to_detect)

        # Rescale the image (get all values between 0 and 1)
        img = img/255.

        pred = loaded_model_1.predict(tf.expand_dims(img, axis=0))

        # Get the predicted class
        if len(pred[0]) > 1:  # check for multi-class
            # if more than one output, take the max
            pred_class = class_names[pred.argmax()]
        else:
            # if only one output, round
            pred_class = class_names[int(tf.round(pred)[0][0])]

        return pred_class