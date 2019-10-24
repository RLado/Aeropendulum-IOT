# Aeropendulum-IOT
**Monitor and control my version of an Aeropendulum remotely.**

This code provides a simple web interface for monitoring the Aeropendulum, in addition to some tools to control it. The code is intended to run on a Raspberry Pi equipped with a USB webcam and a USB-serial connection to the Arduino controlling Aeropendulum.

![WI_beta_pic](https://user-images.githubusercontent.com/25719985/67196905-f7b9ca80-f3fb-11e9-9a70-01eca5c1be0f.png)

[Link to a video of the original project](https://www.youtube.com/watch?v=837XkPRZ9Yc)

---
## How to setup
### Setup using Docker
This is the recommended way to setup the Web Interface.

#### Install the latest version of Docker as instructed here (if necessary): https://docs.docker.com/install/linux/docker-ce/debian/

#### Build the image and run the container at startup
**Note:** *Make sure all the video and serial devices you will need are plugged in at this moment*
```bash
cd Docker_Setup
bash dockerSetup.sh
```
#### Done! Now the container will restart automatically unless stopped.
---
## How to access the container while running
In order to troubleshoot or in case you want to control the AP you will need to access the container previously setup. To do that just do:
```bash
docker exec -it Aeropendulum-IOT bash
```
---
## How to change AP parameters while the Web Interface is running
Make sure **auto-reset** has been **disabled** on the Arduino, you can do that by placing a 120 ohm resistor in the headers between 5v and reset.

Then do:
```bash
docker exec -it Aeropendulum-IOT bash
export AP_ARDUINO_SOURCE=/dev/ttyUSB0 #Change the device if necessary
python WebInterface/AP_command.py 1 45 0.03 0.06 0 #The arguments required in order are: FC (function code 0(off)/1(on)), Target (in degrees), P, I, D
```
---
## Troubleshooting
Check if **runWI.sh** is correctly setup, and if all devices are plugged in.

```bash
export FLASK_APP=WebInterface
export FLASK_DEBUG=1

#Set video device
export OPENCV_CAMERA_SOURCE=0
#Set Arduino serial device
export AP_ARDUINO_SOURCE=/dev/ttyUSB0

#run on the local network
flask run --host=0.0.0.0
```
