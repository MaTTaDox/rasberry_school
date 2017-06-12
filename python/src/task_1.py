#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import datetime  # GPIO-Bibliothek
# oder "from RPi import GPIO"

sensor = Adafruit_DHT.DHT11

pin = 26
delay = 5

def loop():
    while True:
        luftfeuchte, temperatur = Adafruit_DHT.read_retry(sensor, pin)
        messzeit = time.strftime("Am %d.%m.%Y um %H:%M:%S Uhr")
        print '+-------------------------------------------------+'
        print messzeit
        print 'Temperatur: {0:0.1f}°C Luftfeuchtigkeit: {1:0.1f}%'.format(temperatur,luftfeuchte)
        time.sleep(delay)


def run():
    print "Die Messung erfolgt alle %d Sekunden." % delay
    
    while True:
        luftfeuchte, temperatur = Adafruit_DHT.read_retry(sensor, pin)
        messzeit = time.strftime("Am %d.%m.%Y um %H:%M:%S Uhr")
        print '+-------------------------------------------------+'
        print messzeit
        print 'Temperatur: {0:0.1f}°C Luftfeuchtigkeit: {1:0.1f}%'.format(temperatur,luftfeuchte)
        time.sleep(delay)

