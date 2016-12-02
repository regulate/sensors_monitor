#!/usr/bin/python
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import time
import sys

class ConditionSensor(object):

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

class DHT11(object):
    SENSOR = 11

    def __init__(self, pin_num, temp=0.0, humidity=0.0):
        self.humidity=humidity
        self.temp=temp
        self.pin_num = pin_num

    def read_and_get(self):
        self.humidity, self.temp = DHT.read_retry(self.SENSOR, self.pin_num)
        return (self.temp, self.humidity)

    def read_and_print(self):
        self.read_and_get()
        print ("Temp: {self.temp}C, Humidity:{self.humidity}%".format(self = self))
