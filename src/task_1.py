#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
# oder "from RPi import GPIO"

LED_1 = 20
BUTTON_1 = 26
DELAY = 1
LED_STATUS = False


def changelightstate(channel):

    global LED_STATUS

    LED_STATUS = not LED_STATUS

    GPIO.output(LED_1, LED_STATUS)


def run():
    GPIO.setup(LED_1, GPIO.OUT)   # Pin als Ausgang verwenden
    GPIO.setup(BUTTON_1, GPIO.IN)    # Pin als Ausgang verwenden

    GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=changelightstate)

    while True:
        ""


