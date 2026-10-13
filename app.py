import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
from keras.models import load_model
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from google import genai

client = genai.Client(api_key="YOU_API_KEY")

app = Flask(__name__)

model_1 =load_model('model.h5')

print('Model loaded. Check http://127.0.0.1:5000/')

labels = {0: 'Healthy', 1: 'Invalid', 2: 'Powdery', 3: 'Rusty'}


def getResult(image_path):
    img = load_img(image_path, target_size=(225,225))
    x = img_to_array(img)
    x = x.astype('float32') / 255.
    x = np.expand_dims(x, axis=0)
    predictions = model_1.predict(x)[0]

    # use it.........................................................................
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[Image.open(image_path), "Predict name of leaf and Detail disease severity, treatment (bullet points, <500 chars) step-by-step, don't give bold letters in response. Also recommend some pesticides or medicines to treat it."])
    diagnosis = response.text.strip()

    return predictions, diagnosis

@app.route('/', methods=['GET'])
def index():
    return render_template('index_copy.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        predictions, diagnosis =getResult(file_path)
        predicted_label = labels[np.argmax(predictions)]
        # print("\n",diagnosis)
        return jsonify({'label': predicted_label, 'solution': diagnosis.split('*')})
    return jsonify({'label': '', 'solution': ''})


if __name__ == '__main__':
    app.run(debug=True)


