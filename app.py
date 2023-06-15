import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import tensorflow as tf
import cv2
import download_model

download_model.download()

app = Flask(__name__)
model =tf.keras.models.load_model('models/saved_model')
img_size= 180

from PIL import Image
def filestorage_to_array(file_storage):
    # Open the image using PIL
    image = Image.open(file_storage)
    image_array = np.array(image)
    return image_array

@app.route('/')
def home():
    return render_template('index.html',prediction_text="")

@app.route('/predict',methods=['POST'])
def predict():
    picture = request.files["selectedPicture"]

    image_array = filestorage_to_array(picture)
    data = cv2.resize(np.array(image_array), (img_size,img_size))
    data_reshaped = np.reshape(data, (1,img_size,img_size,3))
    pred_prob = model.predict(data_reshaped)
    pred = np.argmax(pred_prob,axis=1)[0]
    labels = ["Glioma Tumor", "Meningioma Tumor",	"No Tumor",	"Pituitary Tumor"]
    predicted = labels[pred]

    return render_template('index.html', prediction_text=predicted)


if __name__ == "__main__":
    app.run(debug=True)