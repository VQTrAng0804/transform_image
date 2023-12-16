from flask import Flask, render_template, request, redirect
from help import reflection, grayscale, sepia, deep_blur, paler_blur, deep_pencil_sketch, paler_pencil_sketch
from help import delete_back, negative, vintage, fresh, edges, bland
from werkzeug.utils import secure_filename
import os
import base64
import cv2


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the uploads directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def apply_effect(image_path, effect):
    image = cv2.imread(image_path)

    if effect == 'reflection':
        image = reflection(image)
    elif effect == 'grayscale':
        image = grayscale(image)
    elif effect == 'sepia':
        image = sepia(image)
    elif effect == 'deep blur':
        image = deep_blur(image)
    elif effect == 'paler blur':
        image = paler_blur(image)
    elif effect == 'deep pencil sketch':
        image = deep_pencil_sketch(image)
    elif effect == 'paler pencil sketch':
        image = paler_pencil_sketch(image)
    elif effect == 'delete back ground':
        image = delete_back(image)
    elif effect == 'negative':
        image = negative(image)
    elif effect == 'vintage':
        image = vintage(image)
    elif effect == 'fresh':
        image = fresh(image)
    elif effect == 'edges':
        image = edges(image)
    elif effect == 'bland':
        image = bland(image)

    # Convert the image to base64 for displaying in HTML
    _, img_encoded = cv2.imencode('.png', image)
    img_str = base64.b64encode(img_encoded).decode("utf-8")

    return img_str

@app.route("/", methods=['GET', 'POST'])
def index():
    # Post image from computer
    if request.method == 'POST':
        effect = request.form.get('effect', 'original')

        if 'image' not in request.files:
            return redirect(request.url)

        file = request.files['image']

        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Apply the selected effect to the uploaded image
            image = apply_effect(file_path, effect)

            # Return upload.html with transformed image
            return render_template("upload.html", img_str=image)

    # If it's a GET request, just render the form
    return render_template("index.html")


# See preview by click "Preview" button
@app.route("/preview")
def preview():
    return render_template("preview.html")

