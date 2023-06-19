import numpy as np
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import os
from PIL import Image

IMG_SIZE= 180

def file_exists():
    return os.path.exists(os.getcwd()+"/models/saved_model/variables/variables.data-00000-of-00001")
if not file_exists():
    raise Exception("Please download the model.")
    # You can download from here: https://www.kaggle.com/code/abdullahkavakli/brain-tumor-classification-with-cnn/output?scriptVersionId=125026100
    # The file is variables.data-00000-of-00001
    # Place it under /models/saved_model/variables/

model = tf.keras.models.load_model('models/saved_model')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',prediction_text="")

@app.route('/predict',methods=['POST'])
def predict():
    try:
        picture = request.files["selectedPicture"]
        image = Image.open(picture)
        image_resized = image.resize((IMG_SIZE, IMG_SIZE))
        
        data = np.array(image_resized)
        data_reshaped = np.reshape(data, (1,IMG_SIZE,IMG_SIZE,3))
        pred_prob = model.predict(data_reshaped)
        pred = np.argmax(pred_prob,axis=1)[0]
        labels = ["Glioma Tumor", "Meningioma Tumor",	"No Tumor",	"Pituitary Tumor"]
        predicted = labels[pred]
    except Exception as e:
        predicted = str(e)
    return render_template('index.html', prediction_text=predicted)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
