#!/usr/bin/python
# -*- coding: utf-8 -*-

import src.logic as logic

if __name__ == '__main__':  # Programmstart
    logic.setup()
    print 'Programm mit CTRL-C beenden.'
    try:
        logic.run()
    except KeyboardInterrupt:  # wenn 'CTRL-C' gedrückt, dann Ende
        logic.destroy()
