#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import csv
import lib.lcddriver as lcddriver
import Adafruit_DHT
import time
import lib.bmp180 as bmp180

sensor = Adafruit_DHT.DHT11

lcd = lcddriver.lcd()
lcd.lcd_clear()

SENSOR_PIN = 26
RED_LIGHT = 17
BLUE_LIGHT = 27


delay = 5

def run():

    GPIO.setup(RED_LIGHT, GPIO.OUT)
    GPIO.setup(BLUE_LIGHT, GPIO.OUT)
    last_temp = 0

    print "Die Messung erfolgt alle %d Sekunden." % delay

    (chip_id, chip_version) = bmp180.readBmp180Id()

    print "Chip ID     :", chip_id
    print "Chip Version:", chip_version

    print '+-------------------------------------------------+'

    with open('readings.csv', 'w') as readings_file:
        readings_writer = csv.writer(readings_file, delimiter=";")
        readings_writer.writerow(["Messzeit", "Temperatur", "Luftdruck"])

        while True:

            (temperature, pressure) = bmp180.readBmp180()
            messzeit = time.strftime("%d.%m.%y %H:%M:%S")

            print "Messzeit : ", messzeit
            print "Temperatur : ", temperature, "°C"
            print "Luftdruck  : ", pressure, "mbar"
            print "------------------------------"

            readings_writer = csv.writer(readings_file, delimiter=";")
            readings_writer.writerow([messzeit, temperature, pressure])

            GPIO.output(RED_LIGHT, False)
            GPIO.output(BLUE_LIGHT, False)

            luftfeuchte, temperatur = Adafruit_DHT.read_retry(sensor, SENSOR_PIN)

            if temperatur > last_temp:
                GPIO.output(RED_LIGHT, True)
            elif temperatur < last_temp:
                GPIO.output(BLUE_LIGHT, True)
            else:
                GPIO.output(RED_LIGHT, True)
                GPIO.output(BLUE_LIGHT, True)

            last_temp = temperatur

            print 'Temperatur: {0:0.1f}°C '.format(temperatur)
            print 'Luftfeuchtigkeit: {0:0.1f}%'.format(luftfeuchte)
            print '+-------------------------------------------------+'

            string_1 = "{0}|{1:0.1f}C".format(time.strftime("%d.%m %H:%M"), temperature)
            string_2 = "{0:0.1f}%|{1:0.2f}mBar".format(luftfeuchte, pressure)

            lcd.lcd_display_string(string_1, 1)
            lcd.lcd_display_string(string_2, 2)
            time.sleep(delay)

