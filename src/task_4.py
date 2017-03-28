#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
import sys
import max7219.led as led

BUTTON_1 = 26
BUTTON_2 = 19
BUTTON_3 = 13

lkw = 0
pkw = 0

matrix = led.matrix()

RETURN = False


def count(channel):
    global lkw, pkw, matrix

    if channel == BUTTON_1:
        lkw += 1

    if channel == BUTTON_2:
        pkw += 1

    matrix.show_message(str(pkw))
    sys.stdout.write("\r LKW: " + str(lkw) + " PKW: " + str(pkw))
    sys.stdout.flush()


def finish(channel):
        global RETURN

        RETURN = True


def run():

    GPIO.setup(BUTTON_1, GPIO.IN)
    GPIO.setup(BUTTON_2, GPIO.IN)
    GPIO.setup(BUTTON_3, GPIO.IN)

    sys.stdout.write("\r LKW: " + str(lkw) + " PKW: " + str(pkw))
    sys.stdout.flush()

    GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=count)
    GPIO.add_event_detect(BUTTON_2, GPIO.FALLING, callback=count)
    GPIO.add_event_detect(BUTTON_3, GPIO.FALLING, callback=finish)

    while not RETURN:
        ""

