import RPi.GPIO as GPIO
import time
import random

while True

    a = 'abcd'
    n = '1234'

ledPin = 11    # RPI Board pin11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, GPIO.LOW)
	print ('using pin%d'%ledPin)

def loop():
	while True:
		GPIO.output(ledPin, GPIO.HIGH)  # Password created
		print ('...led on')
		time.sleep(1)
		GPIO.output(ledPin, GPIO.LOW) # led off
		print ('led off...')
		time.sleep(1)

def destroy():
	GPIO.output(ledPin, GPIO.LOW)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
