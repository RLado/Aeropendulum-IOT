#Docker Setup: Device STring Party

import subprocess

devs=subprocess.getoutput('ls /dev/video*;ls /dev/ttyUSB*')
devstr=' '
for i in devs.split('\n'):
    devstr+='--device=' + i + ' '
print(devstr)
