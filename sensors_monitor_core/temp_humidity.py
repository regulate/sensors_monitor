#!/usr/bin/python
import sys
import Adafruit_DHT

class DHT11(object):
    SENSOR = 11

    def __init__(self, pin_num, temp=0.0, humidity=0.0):
        self.humidity=humidity
        self.temp=temp
        self.pin_num = pin_num

    def read_and_get(self):
        self.humidity, self.temp = Adafruit_DHT.read_retry(self.SENSOR, self.pin_num)
        return (self.temp, self.humidity)

    def read_and_print(self):
        self.read_and_get()
        print "Temp: {self.temp}C, Humidity:{self.humidity}%".format(self = self)
