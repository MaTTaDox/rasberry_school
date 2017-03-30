#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
import sys
import os
import time

LED_1 = 21
LED_2 = 20
LED_3 = 16


def setlight(red, yellow, green):
    GPIO.output(LED_1, not red)
    GPIO.output(LED_2, not yellow)
    GPIO.output(LED_3, not green)


def check(percent):
    if percent < 20:
        setlight(1, 0, 0)
    elif percent < 40:
        setlight(1, 1, 0)
    elif percent < 50:
        setlight(0, 1, 0)
    elif percent < 80:
        setlight(0, 1, 1)
    else:
        setlight(0, 0, 1)


def run():
    GPIO.setup(LED_1, GPIO.OUT)
    GPIO.setup(LED_2, GPIO.OUT)
    GPIO.setup(LED_3, GPIO.OUT)

    while True:
        s = os.statvfs("/")
        percent = int(float(float(s.f_bavail) / float(s.f_blocks)) * float(100))
        sys.stdout.write("\r"+str(percent)+"%")
        sys.stdout.flush()
        check(percent)
        time.sleep(0.5)

