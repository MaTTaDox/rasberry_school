#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
import sys
import os
import time


def run():
    s = os.statvfs("/")
    percent = (s.f_frsize * s.f_bfree) / (s.f_frsize * s.f_blocks) * 100

    while True:
        sys.stdout.write("\r"+str(percent))
        sys.stdout.flush()
        time.sleep(0.5)

