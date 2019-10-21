export FLASK_APP=WebInterface
export FLASK_DEBUG=1

#Set video device
export OPENCV_CAMERA_SOURCE=0
#Set Arduino serial device
export AP_ARDUINO_SOURCE=/dev/ttyUSB0

#run on the local network
flask run --host=0.0.0.0
