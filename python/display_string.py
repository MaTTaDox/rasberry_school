#!/usr/bin/python
# -*- coding: utf-8 -*-

import src.logic as logic
import sys
import lib.lcddriver as lcddriver

lcd = lcddriver.lcd()
lcd.lcd_clear()


if __name__ == '__main__':  # Programmstart

    try:
        arg = sys.argv[1]
        lcd.lcd_clear()
        lcd.lcd_display_string(str(arg), 1)
        logic.destroy()
    except IndexError:
        print "Ungültige Auswahl"
        logic.destroy()
    except KeyboardInterrupt:  # wenn 'CTRL-C' gedrückt, dann Ende
        print "Programm wird beendet"
        logic.destroy()
