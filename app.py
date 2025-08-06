from flask import Flask, request, render_template
import os
import numpy as np
from PIL import Image, UnidentifiedImageError
import tensorflow as tf
import base64
from io import BytesIO

app = Flask(__name__)

# Load Models
classification_model = tf.keras.models.load_model('classification_model.h5', compile=False)
segmentation_model = tf.keras.models.load_model('Segmentation_model.h5', compile=False)

@app.route('/', methods=['GET', 'POST'])
def home():
    result_text = None
    result_image = None

    if request.method == 'POST':
        mode = request.form.get('mode')
        file = request.files['file']

        if file:
            filepath = os.path.join('uploads', file.filename)
            os.makedirs('uploads', exist_ok=True)
            file.save(filepath)

            try:
                img = Image.open(filepath).convert('RGB')
            except UnidentifiedImageError:
                result_text = "Error: Unsupported file format"
                return render_template('index.html', result_text=result_text)

            original_size = img.size
            img_resized = img.resize((256, 256))
            img_array = np.array(img_resized) / 255.0
            img_input = np.expand_dims(img_array, axis=0)

            if mode == 'classification':
                pred = classification_model.predict(img_input)
                class_idx = np.argmax(pred)
                classes = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']
                result_text = f"Classification Result: {classes[class_idx]}"

            elif mode == 'segmentation':
                mask = segmentation_model.predict(img_input)[0]
                mask = (mask > 0.5).astype(np.uint8).squeeze()

                mask_img = Image.fromarray(mask * 255).resize(original_size)
                mask_array = np.array(mask_img)

                orig_img_array = np.array(img)
                orig_img_array[mask_array > 127] = [255, 0, 0]  # Red overlay

                result_img = Image.fromarray(orig_img_array)

                buffered = BytesIO()
                result_img.save(buffered, format="JPEG")
                result_image = base64.b64encode(buffered.getvalue()).decode()

                result_text = "Segmentation Completed"

    return render_template('index.html', result_text=result_text, result_image=result_image)

if __name__ == '__main__':
    app.run(debug=True)
