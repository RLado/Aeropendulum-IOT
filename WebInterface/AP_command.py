#AP_command.py
#Aeropendulum control script
#20th October 2019
#Ricard Lado <ricardlador@iqs.edu

import AP_serialCom
import sys

class Missing_Arguments(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


if len(sys.argv)!=6:
    raise(Missing_Arguments('\n\n---------------------\nUsage requires 5 arguments!\nThe arguments required in order are: FC (function code 0(off)/1(on)), Target (in degrees), P, I, D\nexample: python AP_command.py 1 45 0.03 0.06 0 \n---------------------\n'))
    exit()

FC=sys.argv[1]
target=sys.argv[2]
P=sys.argv[3]
I=sys.argv[4]
D=sys.argv[5]
AP_serialCom.AP_write(FC,target,P,I,D)
