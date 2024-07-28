from flask import Flask, request, jsonify, render_template, Response
import subprocess

from main import main  
# from frontend_test import main
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


    heading_txt_path = 'heading.txt'
    story_txt_path = 'story.txt'

    try:
        with open(heading_txt_path, 'w') as file:
            file.write(heading)
    except Exception as e:
        return e

    try:
        with open(story_txt_path, 'w') as file:
            file.write(comment)
    except Exception as e:
        return e


    
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    def generate_output():
        process = subprocess.Popen(
            ['python3', 'main.py', heading_txt_path, story_txt_path, image_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        for line in iter(process.stdout.readline, b''):
            yield line.decode('utf-8')
        for line in iter(process.stderr.readline, b''):
            yield line.decode('utf-8')

    return Response(generate_output(), mimetype='text/plain')

    # # Emit progress update
    # socketio.emit('progress', {'message': 'Starting video generation...'})


    # # Call the process_video function from main.py
    # response = main(heading_txt_path, story_txt_path, image_path)

    # if response['status'] == 'success':
    #     return jsonify(response), 200
    # else:
    #     return jsonify({'status': 'error', 'message': 'Task failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
