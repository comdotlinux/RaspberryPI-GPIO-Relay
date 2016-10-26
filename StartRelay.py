#!/usr/bin/python -x
import RPi.GPIO as GPIO
import sys
#from time import sleep
try:

    GPIO.setmode(GPIO.BOARD)
    try:
        pin_number = int(sys.argv[1])
    except IndexError:
        pin_number = 1
        print "input could not be parsed pin set to %d" % pin_number

    if pin_number > 1:
	print "setting %d pin to low state." % pin_number
        GPIO.setup(pin_number, GPIO.OUT)
        GPIO.output(pin_number, 0)

except:
	print "Other error or exception occurred!"
	GPIO.cleanup()

