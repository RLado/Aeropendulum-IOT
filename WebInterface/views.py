#views.py
#Flask app for the Aeropendulum_IOT project
#8th October 2019
#Ricard Lado <ricardlador@iqs.edu>

from flask import Blueprint, render_template, Response
#Camera
from .camera_opencv import Camera
#Chart modules
from datetime import datetime
import time
import json
#Serial comunications
from multiprocessing import Process, Queue
from WebInterface import AP_serialCom
import math


main=Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

#Start serial read process
readQ=Queue(maxsize=2)
p=Process(target=AP_serialCom.AP_read, args=(readQ,))
p.start()

@main.route('/chart-data')
def chart_data():
    def read_arduino_data():
        while True:
            try:
                if not readQ.empty():
                    lastRead=readQ.get()
                    lrFields=lastRead.split('|')
                json_data = json.dumps(
                    {'time': float(lrFields[4]), 'value': float(lrFields[0])/math.pi*180, 'value2': float(lrFields[1])/math.pi*180})
                yield f'data:{json_data}\n\n'
                time.sleep(0.2)
            except:
                print('Error reading Arduino serial data')

    return Response(read_arduino_data(), mimetype='text/event-stream')

#Video streaming generator function.
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@main.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
