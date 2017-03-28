#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
# oder "from RPi import GPIO"

LED_1 = 21
BUTTON_1 = 26


def run():
    GPIO.setup(LED_1, GPIO.OUT)
    GPIO.setup(BUTTON_1, GPIO.IN)

    while True:
        x = GPIO.input(BUTTON_1)
        print x


