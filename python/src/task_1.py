#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import datetime  # GPIO-Bibliothek
# oder "from RPi import GPIO"

sensor = Adafruit_DHT.DHT11

SENSOR_PIN = 26
RED_LIGHT = 17
BLUE_LIGHT = 27


delay = 10

def run():

    GPIO.setup(RED_LIGHT, GPIO.OUT)
    GPIO.setup(BLUE_LIGHT, GPIO.OUT)

    print "Die Messung erfolgt alle %d Sekunden." % delay

    last_temp = 0

    while True:

        GPIO.output(RED_LIGHT, False)
        GPIO.output(BLUE_LIGHT, False)

        luftfeuchte, temperatur = Adafruit_DHT.read_retry(sensor, SENSOR_PIN)

        if temperatur > last_temp:
            GPIO.output(RED_LIGHT, True)
        elif temperatur < last_temp:
            GPIO.output(BLUE_LIGHT, True)
        else:
            GPIO.output(RED_LIGHT, True)
            GPIO.output(BLUE_LIGHT, True)



        messzeit = time.strftime("Am %d.%m.%Y um %H:%M:%S Uhr")
        print '+-------------------------------------------------+'
        print messzeit
        print 'Temperatur: {0:0.1f}°C Luftfeuchtigkeit: {1:0.1f}%'.format(temperatur,luftfeuchte)
        time.sleep(delay)

