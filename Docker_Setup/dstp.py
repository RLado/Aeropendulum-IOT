import subprocess

vdev=subprocess.getoutput('ls /dev/video*')
devstr=' '
for i in vdev.split('\n'):
    devstr+='--device=' + i + ' '
print(devstr)
