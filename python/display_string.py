#!/usr/bin/python
# -*- coding: utf-8 -*-

import src.logic as logic
import sys
import max7219.led as led
import lib.lcddriver as lcddriver

lcd = lcddriver.lcd()
lcd.lcd_clear()

matrix = led.matrix()


if __name__ == '__main__':  # Programmstart

    try:
        arg = sys.argv[1]

        matrix.show_message(str(arg))
        lcd.lcd_clear()
        lcd.lcd_display_string(str(arg), 1)
        logic.destroy()
    except IndexError:
        print "Ungültige Auswahl"
        logic.destroy()
    except KeyboardInterrupt:  # wenn 'CTRL-C' gedrückt, dann Ende
        print "Programm wird beendet"
        logic.destroy()
