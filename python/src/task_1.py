#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import datetime  # GPIO-Bibliothek
# oder "from RPi import GPIO"

pin = 26
delay = 5


def run():

    while True:
        ""
