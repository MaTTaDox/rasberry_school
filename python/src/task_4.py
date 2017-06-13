#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import lib.mysql.use as mysqlUse
import os
import datetime  # GPIO-Bibliothek
import lib.mysql.init as mysqlInit
# oder "from RPi import GPIO"

sensor = Adafruit_DHT.DHT11

delay = 10

def getLocation(identifer):
    query = mysqlUse.execute("SELECT id FROM locations WHERE identifer = '"+identifer+"' LIMIT 1")
    row = query.fetchone()

    if row is None:
        mysqlUse.execute("INSERT INTO locations (identifer) VALUES('"+identifer+"')")

        query = mysqlUse.execute("SELECT id FROM locations WHERE identifer = '"+identifer+"' LIMIT 1")
        row = query.fetchone()

    return row[0]


def run():

    mysqlInit.db()

    location = raw_input("Messort:")

    while True:
        ""


