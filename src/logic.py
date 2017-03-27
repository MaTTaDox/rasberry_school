#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Aufgabenstellung

        Blinklichter werden oft als Warnung bei gef�hrlichen
        Vorg�ngen eingesetzt.

        Beim Start soll die LED blinken.

'''
import RPi.GPIO as GPIO  # GPIO-Bibliothek
# oder "from RPi import GPIO"

import sys


# globale Variablen festlegen
LED_1 = 20
BUTTON_1 = 26
DELAY = 1
LED_STATUS = False


def setup():
    GPIO.setmode(GPIO.BCM)        # GPIO-Nummer verwenden
    GPIO.setwarnings(False)       # Warnungen ausschalten
    GPIO.setup(LED_1, GPIO.OUT)   # Pin als Ausgang verwenden
    GPIO.setup(BUTTON_1, GPIO.IN)    # Pin als Ausgang verwenden


def destroy():
    GPIO.cleanup()                      # RESET, GPIO-Pins freigeben
    sys.exit()


def changelightstate(channel):

        global LED_STATUS

        LED_STATUS = not LED_STATUS

        GPIO.output(LED_1, LED_STATUS)



def run():
    GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=changelightstate)

    while True:
        ""


