#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
import time

#Ampel
LED_1_red = 21
LED_2_yellow = 20
LED_3_green = 16

#Fussgaenger Ampel
LED_4_red = 23
LED_5_green = 24

#Knoepfe und sonstiges
BUTTON_1 = 26
BUTTON_2 = 19
BUTTON_4 = 6
endTask = 1
checkAmpelRot = False
checkFuessgaengerAmpelRot = False


def fussgaengerAmpel():
    if LED_1_red == 0 :
        if(LED_5_green == 0):
            ""
        else:
            GPIO.output(LED_5_green)
    elif(LED_3_green == 0):
        time.sleep(5)
        GPIO.output(LED_3_green)
        GPIO.output(LED_2_yellow)
        time.sleep(3)
        GPIO.output(LED_2_yellow)
        GPIO.output(LED_1_red)
        GPIO.output(LED_5_green)
        time.sleep(10)
        GPIO.output(LED_5_green)
        GPIO.output(LED_4_red)
        startAmpelSystem()


def startAmpelSystem():
    GPIO.output(LED_5_green)
    GPIO.output(LED_2_yellow)
    GPIO.output(LED_4_red)
    time.sleep(3)
    GPIO.output(LED_1_red)
    GPIO.output(LED_2_yellow)
    GPIO.output(LED_3_green)
    time.sleep(15)
    GPIO.output(LED_3_green)
    GPIO.output(LED_2_yellow)
    time.sleep(3)
    GPIO.output(LED_2_yellow)
    GPIO.output(LED_1_red)
    GPIO.Output(LED_4_red)
    GPIO.output(LED_5_green)

def end():
    global endTask
    endTask = 0

def run():
    GPIO.setup(LED_1_red, GPIO.OUT)
    GPIO.setup(LED_2_yellow, GPIO.OUT)
    GPIO.setup(LED_3_green, GPIO.OUT)
    GPIO.setup(LED_4_red, GPIO.OUT)
    GPIO.setup(LED_5_green, GPIO.OUT)
    GPIO.setup(BUTTON_1, GPIO.IN)
    GPIO.setup(BUTTON_2, GPIO.IN)
    GPIO.setup(BUTTON_4, GPIO.IN)

    GPIO.output(LED_1_red)
    checkAmpelRot = True
    GPIO.output(LED_4_red)
    checkFuessgaengerAmpelRot = True

    GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=startAmpelSystem)
    GPIO.add_event_detect(BUTTON_2, GPIO.FALLING, callback=fussgaengerAmpel)
    GPIO.add_event_detect(BUTTON_4, GPIO.FALLING, callback=end)

    while endTask == 1:
        ""