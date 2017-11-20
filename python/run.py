#!/usr/bin/python
# -*- coding: utf-8 -*-

import lib.mysql.init as myysql

if __name__ == '__main__':

    myysql.db()

    try:
        print 'Programm mit CTRL-C beenden.'
        while True:
            True
    except IndexError:
        print "Ungültige Auswahl"
        logic.destroy()
    except KeyboardInterrupt:  # wenn 'CTRL-C' gedrückt, dann Ende
        print "Programm wird beendet"
        logic.destroy()
