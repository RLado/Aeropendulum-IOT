#AP_serialCom.py
#Aeropendulum serial comunications module
#20th October 2019
#Ricard Lado <ricardlador@iqs.edu

import os
import serial
from multiprocessing import Process, Queue
import math
import time

'''
The AVR Arduinos (Uno, Nano, Mega) have auto-reset function. At opening
of USB connection the circuit around USB resets the MCU. After reset the
bootloader waits a second for a new upload. If the upload doesn't happen
the bootloader starts the current sketch.
The serial.Serial() command in python opens the USB connection. With that
the Arduino is reset and waits in bootloader while you send the data. The
data doesn't arrive to the sketch.
----------------------------------------------------------------------------
HOW TO SOLVE:

The simple way that doesn't require any permanent modifying of your hardware or
software configuration changes:

Stick a 120 ohm resistor in the headers between 5v and reset (you can find these
on the isp connector too). 120 is hard to find so just combine resistors. Don't
go below 110 ohms or above 124 ohms, and don't do this with an isp programmer
attached. You can just pull out the resistor when you want auto-reset back.
'''

#Serial port
port=os.environ['AP_ARDUINO_SOURCE']
#Create lock file for the serial port
with open('/dev/shm/SerLockAP.lock','w') as lockfile:
    lockfile.write('0')

#Create lock and unlock functions
def lock():
    with open('/dev/shm/SerLockAP.lock','w') as lockfile:
        lockfile.write('1')

def unlock():
    with open('/dev/shm/SerLockAP.lock','w') as lockfile:
        lockfile.write('0')
        time.sleep(2) #Ensures it is not reading (Could be improved by locking on read)

def islocked():
    with open('/dev/shm/SerLockAP.lock','r') as lockfile:
        if lockfile.read()!='0':
            return True
        else:
            return False

#Read and write serial funcions that can be used simultaneously
def AP_read(out_q):
    while True: #loop around while locked
        if not islocked():
            with serial.Serial(port, 115200, timeout=1) as ser:
                while True:
                    line = ser.readline()   # read a '\n' terminated line
                    if len(line)>0:
                        try:
                            out_q.put(line.decode('utf-8'))
                        except UnicodeDecodeError:
                            print('Decode Error')
                    #Check lock file, if locked stop reading
                    if islocked():
                        break

def AP_write(FC,target,P,I,D):
    while islocked(): #Check if is already locked
        pass
    lock() #Lock the port while writing
    with serial.Serial(port, 115200, timeout=1) as ser:
        cmd=f'#{FC}#{round(float(target)/180*math.pi,6)}#{P}#{I}#{D}'
        ser.write(cmd.encode('utf-8'))
    unlock() #Unlock the port to allow reading


#Main reads the serial port
if __name__ == '__main__':
    queue=Queue(maxsize=1)
    p=Process(target=AP_read, args=(queue,))
    p.start()

    while True:
        if not queue.empty():
            print(queue.get())

    p.terminate()
