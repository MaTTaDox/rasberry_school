#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
# oder "from RPi import GPIO"

import sys


def setup():
    GPIO.setmode(GPIO.BCM)        # GPIO-Nummer verwenden
    GPIO.setwarnings(False)       # Warnungen ausschalten


def destroy():
    GPIO.cleanup()                      # RESET, GPIO-Pins freigeben
    sys.exit()

