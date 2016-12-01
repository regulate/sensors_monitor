#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class HCSR501(object):

    def __init__(self, pin_num):
        super(HCSR501, self).__init__()
        self.state = False
        self.prev_state = False
        self.pin_num = pin_num
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_num, GPIO.IN)

    def detect_and_get(self):
        self.prev_state = self.state;
        self.state = True if GPIO.input(self.pin_num)==1 else False
        return self.state

    def monitor(self, monitor_step=0.5):
        print ("Monitoring started")
        try:
            # Loop until users quits with CTRL-C
            while True :
                # Read PIR state
                self.detect_and_get()
                if self.state==True and self.prev_state==False:
                    # PIR is triggered
                    print ("Motion detected!")
                elif self.state==False and self.prev_state==True:
                    # REED has returned to ready state
                    print ("Ready")
                time.sleep(monitor_step)
        except KeyboardInterrupt:
            print ("Quit")
            # Reset GPIO settings
            GPIO.cleanup()
