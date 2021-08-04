import serial
import requests
# print('serial' + serial.__version__)

PORT = '/dev/cu.usbserial-1410' 
# PORT = '/dev/ttyUSB0'
BAUDRATE = 9600
ser = serial.Serial(PORT, BAUDRATE)

#def fireDetection() : 
def sensorRead(str) :
    str = str.decode()
    str = str.rstrip('\n')
    if len(str) == 6 : 
        # PEACE
        return False
    else :
        # WARNING
        return True

while True :
    line = ser.readline()    
    if sensorRead(line) :
        print("warning signal") # temp signal
        r = requests.put(url='http://210.204.38.60:8080/api/fire/break-out/3') # tempURI
        # r = requests.put(url='ec2-52-78-90-230.ap-northeast-2.compute.amazonaws.com/api/fire/break-out/3')

    else :
        print("peace")
        # return False

# ls -l /dev/ttyU*
# http://210.204.38.60:8080/api/fire/break-out/2