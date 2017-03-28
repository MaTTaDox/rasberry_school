#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # GPIO-Bibliothek
import sys
import os
import time


def run():
    s = os.statvfs("/")
    percent = (s.f_blocks - s.f_bfree) * 100 / (s.f_blocks - s.f_bfree + s.f_bavail) + 1

    while True:
        sys.stdout.write("\r"+str(percent))
        sys.stdout.flush()
        time.sleep(0.5)

