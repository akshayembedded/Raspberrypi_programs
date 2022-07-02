import RPi.GPIO as a
import time
a.setmode(a.BCM)
a.setup(14,a.IN,a.PUD_UP)
a.setup(15,a.OUT)
while 1:
    if(a.input(14)==0):
        a.output(15,1)
        print("ledON")
        time.sleep(1)
    else:
        a.output(15,0)
        print("LED OFF")
