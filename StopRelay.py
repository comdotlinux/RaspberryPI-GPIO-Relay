#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
#from time import sleep
try:
		
    pin_number = int(sys.argv[1])
    GPIO.setmode(GPIO.BOARD)
    if int(sys.argv[1]) >= 1:
	print "setting %d pin to high state." % pin_number
        GPIO.setwarnings(False)
        GPIO.setup(pin_number, GPIO.OUT)
        GPIO.output(12, 1)

except:
	print "Other error or exception occurred!"
	GPIO.cleanup()

