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
checkTrafficLightRed = True
checkPassengerTrafficLightRed = False


def fussgaengerTrafficLight(channel):
    global checkTrafficLightRed
    global checkPassengerTrafficLightRed

    if(checkTrafficLightRed == True):
        GPIO.output(LED_5_green, False)
    elif(checkTrafficLightRed == False):
        time.sleep(5)
        GPIO.output(LED_3_green, True)
        GPIO.output(LED_2_yellow, False)
        time.sleep(3)
        GPIO.output(LED_2_yellow, True)
        GPIO.output(LED_1_red, False)
        checkTrafficLightRed = True
        time.sleep(2)
        GPIO.output(LED_4_red, True)
        GPIO.output(LED_5_green, False)
        checkPassengerTrafficLightRed = False

def startTrafficLightSystem(channel):
    global checkTrafficLightRed
    global checkPassengerTrafficLightRed

    GPIO.output(LED_5_green, True)
    GPIO.Output(LED_4_red, False)
    GPIO.output(LED_2_yellow, False)
    checkPassengerTrafficLightRed = True
    time.sleep(3)
    GPIO.output(LED_1_red, True)
    GPIO.output(LED_2_yellow, True)
    GPIO.output(LED_3_green, False)
    checkTrafficLightRed = False
    time.sleep(15)
    GPIO.output(LED_5_green, True)
    GPIO.output(LED_2_yellow, False)
    time.sleep(3)
    GPIO.output(LED_2_yellow, True)
    GPIO.output(LED_1_red, False)
    GPIO.output(LED_4_red, True)
    GPIO.output(LED_5_green, False)
    checkTrafficLightRed = True
    checkPassengerTrafficLightRed = False


def endTaskProcess(channel):
    global endTask
    endTask = 0


def run():
    global checkTrafficLightRed
    global checkPassengerTrafficLightRed

    GPIO.setup(LED_1_red, GPIO.OUT)
    GPIO.setup(LED_2_yellow, GPIO.OUT)
    GPIO.setup(LED_3_green, GPIO.OUT)
    GPIO.setup(LED_4_red, GPIO.OUT)
    GPIO.setup(LED_5_green, GPIO.OUT)
    GPIO.setup(BUTTON_1, GPIO.IN)
    GPIO.setup(BUTTON_2, GPIO.IN)
    GPIO.setup(BUTTON_4, GPIO.IN)

    GPIO.output(LED_1_red, False)
    checkTrafficLightRed = True
    GPIO.output(LED_5_green, False)
    checkPassengerTrafficLightRed  = False

    GPIO.add_event_detect(BUTTON_1, GPIO.FALLING, callback=startTrafficLightSystem)
    GPIO.add_event_detect(BUTTON_2, GPIO.FALLING, callback=fussgaengerTrafficLight)
    GPIO.add_event_detect(BUTTON_4, GPIO.FALLING, callback=endTaskProcess)

    while endTask == 1:
        ""