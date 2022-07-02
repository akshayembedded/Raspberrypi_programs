import RPi.GPIO as a
import time
a.setmode(a.BCM)
pins=(2,3,18,5,6,7,14)
digit=(23,24)
for i in pins:
	a.setup(i,a.OUT)
a.setup(23,a.OUT)
a.setup(24,a.OUT)

seg=((1,1,1,1,1,1,0), 
          (0,1,1,0,0,0,0),
         (1,1,0,1,1,0,1),
         (1,1,1,1,0,0,1),
         (0,1,1,0,0,1,1),
         (1,0,1,1,0,1,1),
         (1,0,1,1,1,1,1),
         (1,1,1,0,0,0,0),
         (1,1,1,1,1,1,1),
         (1,1,1,0,0,1,1)
    )


def segment(k,j):
    a.output(23,1)
    a.output(24,0)
    for i in range(0,7): #i=0:
        a.output(pins[i],seg[j][i]) #a.output(pins[0],seg[1][6]
    time.sleep(0.01)#
    a.output(23,0)
    a.output(24,1)
    for i in range(0,7): #i=0:
        a.output(pins[i],seg[k][i]) #a.output(pins[0],seg[1][6]
    time.sleep(0.01)# 1s=0.02*50
while 1:
    segment(3,5)
                

