import RPi.GPIO as GPIO
from time import sleep

def Blinking(timeOut):
	GPIO.output(LEDPin, True)
	sleep(timeOut)
	GPIO.output(LEDPin, False)
	sleep(timeOut)

LEDPin = 19
ButtonPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
	while True:
		# Button pressed
		if GPIO.input(ButtonPin):
			Blinking(0.1)
		else:
			Blinking(1)
finally:
	GPIO.output(LEDPin, False)
	GPIO.cleanup()