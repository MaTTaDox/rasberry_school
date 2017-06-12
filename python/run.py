#!/usr/bin/python
# -*- coding: utf-8 -*-

import src.logic as logic


if __name__ == '__main__':  # Programmstart
    logic.setup()
    options = []

    print "Wähle den Task\n" \


    chased_task = input("Wähle:")

    try:
        task = options[chased_task]
        print 'Programm mit CTRL-C beenden.'
        task.run()
    except IndexError:
        print "Ungültige Auswahl"
        logic.destroy()
    except KeyboardInterrupt:  # wenn 'CTRL-C' gedrückt, dann Ende
        print "Programm wird beendet"
        logic.destroy()
