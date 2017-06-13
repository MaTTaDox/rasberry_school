#!/usr/bin/python
# -*- coding: utf-8 -*-

import lib.mysql.use as mysqlUse
import lib.mysql.init as mysqlInit
import RPi.GPIO as GPIO
import csv
import Adafruit_DHT
import time
import lib.bmp180 as bmp180


delay = 10

sensor = Adafruit_DHT.DHT11

lcd = lcddriver.lcd()
lcd.lcd_clear()

SENSOR_PIN = 26
RED_LIGHT = 17
BLUE_LIGHT = 27

def getLocation(identifer):
    query = mysqlUse.execute("SELECT id FROM locations WHERE identifer = '"+identifer+"' LIMIT 1")
    row = query.fetchone()

    if row is None:
        mysqlUse.execute("INSERT INTO locations (identifer) VALUES('"+identifer+"')")

        query = mysqlUse.execute("SELECT id FROM locations WHERE identifer = '"+identifer+"' LIMIT 1")
        row = query.fetchone()

    return row[0]


def inserRow(locationId, unit, value):

    mysqlUse.execute("INSERT INTO `values` (location_id,unit,`value`) VALUES ('"+locationId+"','"+unit+"','"+value+"')")


def run():

    mysqlInit.db()

    location = raw_input("Messort:")
    locationId = getLocation(location)

    while True:
        (temperature, pressure) = bmp180.readBmp180()
        (humidity, temperatur) = Adafruit_DHT.read_retry(sensor, SENSOR_PIN)

        messzeit = time.strftime("%d.%m.%y %H:%M:%S")

        print "Messzeit : ", messzeit
        print "Temperatur : ", temperature, "°C"
        print "Luftdruck  : ", pressure, "mbar"
        print "------------------------------"
        print 'Temperatur: {0:0.1f}°C '.format(temperatur)
        print 'Luftfeuchtigkeit: {0:0.1f}%'.format(humidity)
        print '+-------------------------------------------------+'

        string_1 = "{0}|{1:0.1f}C".format(time.strftime("%d.%m %H:%M"), temperature)
        string_2 = "{0:0.1f}%|{1:0.2f}mBar".format(humidity, pressure)

        lcd.lcd_display_string(string_1, 1)
        lcd.lcd_display_string(string_2, 2)

        inserRow(locationId, "temperature", temperature)
        inserRow(locationId, "humidity", humidity)
        inserRow(locationId, "pressure", pressure)

        time.sleep(delay)


