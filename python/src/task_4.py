#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
import sys
import lib.multilineMAX7219 as LEDMatrix
import lib.lcddriver as lcddriver

BUTTON_1 = 26
BUTTON_2 = 19
BUTTON_3 = 13

lkw = 0
pkw = 0

LEDMatrix.init()

lcd = lcddriver.lcd()
lcd.lcd_clear()

RETURN = False


def count(channel):
    global lkw, pkw

    if channel == BUTTON_1:
        lkw += 1

    if channel == BUTTON_2:
        pkw += 1

    LEDMatrix.static_message(str(pkw))
    lcd.lcd_clear()
    lcd.lcd_display_string("\r LKW: " + str(lkw) + " PKW: " + str(pkw), 1)
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

    GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=count, bouncetime=200)
    GPIO.add_event_detect(BUTTON_2, GPIO.FALLING, callback=count, bouncetime=200)
    GPIO.add_event_detect(BUTTON_3, GPIO.FALLING, callback=finish, bouncetime=200)

    while not RETURN:
        ""
