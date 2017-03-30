#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
import time

LED_1 = 21
BUTTON_1 = 26
LED_STATE = True


def changelight():
    global LED_STATE

    LED_STATE = not LED_STATE

    GPIO.output(LED_1, LED_STATE)


def run():
    GPIO.setup(LED_1, GPIO.OUT)
    GPIO.setup(BUTTON_1, GPIO.IN)

    while True:
        x = GPIO.input(BUTTON_1)
        if x == 1:
            changelight()
        elif x == 0 and LED_STATE is False:
            changelight()
        time.sleep(0.5)


