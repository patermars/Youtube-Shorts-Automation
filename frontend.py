from flask import Flask, request, jsonify, render_template
from main import process_video  # Import the process_video function from main.py
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    heading = request.form['heading']
    comment = request.form['comment']
    image = request.files['image']
    
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    # Call the process_video function from main.py
    final_output_path = process_video(heading, comment, image_path)

    return jsonify({"message": "Video generated successfully!", "video_path": final_output_path})

if __name__ == '__main__':
    app.run(debug=True)
