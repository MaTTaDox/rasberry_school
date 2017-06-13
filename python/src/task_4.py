#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import datetime  # GPIO-Bibliothek
import lib.mysql.init as mysqlInit
# oder "from RPi import GPIO"

sensor = Adafruit_DHT.DHT11

delay = 10


def run():

    mysqlInit.db()

    while True:
        time.sleep(delay)

