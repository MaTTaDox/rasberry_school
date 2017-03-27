#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Aufgabenstellung

        Blinklichter werden oft als Warnung bei gef�hrlichen
        Vorg�ngen eingesetzt.

        Beim Start soll die LED blinken.

'''
import RPi.GPIO as GPIO  # GPIO-Bibliothek
# oder "from RPi import GPIO"

import time              # wird für sleep benötigt -> time.sleep(0.5)
# oder "from time import sleep" -> sleep(0.5)
import sys



def setup():
    GPIO.setmode(GPIO.BCM)        # GPIO-Nummer verwenden
    GPIO.setwarnings(False)       # Warnungen ausschalten
    GPIO.setup(LED_1, GPIO.OUT)   # Pin als Ausgang verwenden


def destroy():
    GPIO.cleanup()                      # RESET, GPIO-Pins freigeben
    sys.exit()


def loop():

    while True:
        GPIO.output(LED_1,False)
        time.sleep(DELAY)
        GPIO.output(LED_1,True)
        time.sleep(DELAY)
