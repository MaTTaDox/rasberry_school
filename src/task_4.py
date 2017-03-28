#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
import time
import sys

BUTTON_1 = 26
BUTTON_2 = 19
BUTTON_3 = 13

lkw = 0
pkw = 0

RETURN = False


def count(channel):
    global lkw,pkw

    if channel == BUTTON_1:
        lkw += 1

    if channel == BUTTON_2:
        pkw += 1


def finish(channel):
        global RETURN

        RETURN = True


def run():
    GPIO.setup(BUTTON_1,2 GPIO.IN)
    GPIO.setup(BUTTON_2, GPIO.IN)
    GPIO.setup(BUTTON_3, GPIO.IN)

    GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=count)
    GPIO.add_event_detect(BUTTON_2, GPIO.FALLING, callback=count)
    GPIO.add_event_detect(BUTTON_3, GPIO.FALLING, callback=finish)

    while not RETURN:
        sys.stdout.write("\r LKW: " + str(lkw) + " PKW: " + str(pkw))
        sys.stdout.flush()
        time.sleep(0.5)


