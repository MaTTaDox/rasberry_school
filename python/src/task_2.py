#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import csv
import lib.bmp180 as bmp180

delay = 2


def run():


    print "Die Messung erfolgt alle %d Sekunden." % delay

    (chip_id, chip_version) = bmp180.readBmp180Id()

    print "Chip ID     :", chip_id
    print "Chip Version:", chip_version

    print "------------------------------"

    with open('readings.csv', 'w') as readings_file:
        readings_writer = csv.writer(readings_file, delimiter=";")
        readings_writer.writerow(["Messzeit", "Temperatur", "Luftdruck"])

        while True:

            (temperature, pressure) = bmp180.readBmp180()
            messzeit = time.strftime("%d.%m.%Y %H:%M:%S")

            print "Messzeit : ", messzeit
            print "Temperatur : ", temperature, "°C"
            print "Luftdruck  : ", pressure, "mbar"
            print "------------------------------"

            readings_writer = csv.writer(readings_file, delimiter=";")
            readings_writer.writerow([messzeit, temperature, pressure])

            time.sleep(delay)

