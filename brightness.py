import RPi.GPIO as a
a.setmode(a.BCM)
a.setup(18,a.OUT)
p=a.PWM(18,500)#2s
p.start(100)
a.setup(14,a.OUT)
a.setup(15,a.OUT)
a.output(14,1)
a.output(15,0)
while 1:
	d=int(input("Duty Cycle : "))
	p.ChangeDutyCycle(d)
