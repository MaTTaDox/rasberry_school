#!/usr/bin/python
# -*- coding: utf-8 -*-

"""     Aufgabenstellung

        Blinklichter werden oft als Warnung bei gef�hrlichen
        Vorg�ngen eingesetzt.

        Beim Start soll die LED blinken.

"""

import src.logic as logic

if __name__ == '__main__':  # Programmstart
    logic.setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        logic.loop()
    except KeyboardInterrupt:  # wenn 'CTRL-C' gedrückt, dann Ende
        logic.destroy()
