#sonar obstacle avoiding bot in python

#import required Python libraries
import time
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 23

MLEFT = 4
MRIGHT = 25
e1 = 17 
e2 =10 

#set pins as output and input
GPIO.setwarnings(False)                 #Disable warnings
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)	#Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)		#Echo

#Set trigger to false(low)
GPIO.output(GPIO_TRIGGER, False)

#allow module to settle
time.sleep(0.5)

def sonar(n):
	#send 10 us pulse to trigger
	GPIO.output(GPIO_TRIGGER,True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	start = time.time()

	#this doesn't allow for timeout!

	while GPIO.input(GPIO_ECHO)==0:
		start = time.time()

	while GPIO.input(GPIO_ECHO)==1:
		stop = time.time()
	
	#calculate pulse lenght
	elapsed = stop - start

	#distance pulse travelled in that time in time
	#multiplied by the speed of sound (cm/s)
	distance = elapsed * 34000

	#that was the distance there and back so halve the value
	distance = distance / 2
	
	return distance

GPIO.setup(MLEFT, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(MRIGHT, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(e1, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(e2, GPIO.OUT)
GPIO.setwarnings(False)
time.sleep(1)

while True:

	time.sleep(0.3)

	distance = sonar (0)
	print distance

	if(distance >17):
		#foward
		GPIO.output(e1, 1)
		GPIO.output(e2, 1)
		GPIO.output(MLEFT, 1)
		GPIO.output(MRIGHT,1)

	elif(distance <13):
		#backward
		GPIO.output(e1, 1)
		GPIO.output(e2, 1)
		GPIO.output(MLEFT, 0)
		GPIO.output(MRIGHT,0)

	elif(12.9<distance<16.9):
		#stop
		GPIO.output(e1, 0)
		GPIO.output(e2, 0)
