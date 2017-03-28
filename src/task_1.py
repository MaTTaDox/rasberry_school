#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
# oder "from RPi import GPIO"

LED_1 = 21
LED_2 = 20
LED_3 = 16

BUTTON_1 = 26
BUTTON_2 = 19
BUTTON_3 = 13
BUTTON_4 = 6

DELAY = 1


def activatelight(channel):

    mapping = {BUTTON_1: LED_1, BUTTON_2: LED_2, BUTTON_3: LED_3}
    try:
        GPIO.output(mapping[channel], False)
    except IndexError:
        print "Ungültige Knopf"


def disablelights(channel):
    GPIO.output(LED_1, True)
    GPIO.output(LED_2, True)
    GPIO.output(LED_3, True)


def run():
    GPIO.setup(LED_1, GPIO.OUT)   # Pin als Ausgang verwenden
    GPIO.setup(BUTTON_1, GPIO.IN)    # Pin als Ausgang verwenden

    GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=activatelight)
    GPIO.add_event_detect(BUTTON_2, GPIO.FALLING, callback=activatelight)
    GPIO.add_event_detect(BUTTON_3, GPIO.FALLING, callback=activatelight)
    GPIO.add_event_detect(BUTTON_4, GPIO.FALLING, callback=disablelights)

    while True:
        ""


