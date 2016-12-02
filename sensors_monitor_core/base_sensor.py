#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class StateSensor(object):

    def __init__(self, pin_num, name):
        self.name = name
        self.state = None
        self.prev_state = None
        self.pin_num = pin_num
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_num, GPIO.IN)

    def detect_and_get(self):
        self.prev_state = self.state;
        self.state = GPIO.input(self.pin_num)
        return self.state

    def monitor(self, monitor_step=0.5):
        print (self.name + ": monitoring started")
        try:
            # Loop until users quits with CTRL-C
            while True :
                # Read PIR state
                self.detect_and_get()
                if self.state==1 and self.prev_state==0:
                    # PIR is triggered
                    print (self.name + ": state changed to 1")
                elif self.state==False and self.prev_state==True:
                    # REED has returned to ready state
                    print (self.name + ": state changed to 0")
                time.sleep(monitor_step)
        except KeyboardInterrupt:
            print ("Quit")
            # Reset GPIO settings
            GPIO.cleanup()
