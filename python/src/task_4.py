#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import datetime  # GPIO-Bibliothek
# oder "from RPi import GPIO"

sensor = Adafruit_DHT.DHT11



delay = 10

def run():

    while True:
        time.sleep(delay)

