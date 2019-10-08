#views.py
#Flask app for the Aeropendulum_IOT project
#8th August 2019
#Ricard Lado <ricardlador@iqs.edu>

from flask import Blueprint, render_template, Response
#Camera
from .camera_opencv import Camera
#Chart modules
from datetime import datetime
import time
import json
#Debug and test libraries
import random


main=Blueprint('main',__name__)

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': random.random() * 100, 'value2': random.random() * 100})
            yield "data:%s\n\n"%json_data
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')

#Video streaming generator function.
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@main.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
