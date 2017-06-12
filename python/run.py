#!/usr/bin/python
# -*- coding: utf-8 -*-

import src.logic as logic
import src.task_1 as task_1

if __name__ == '__main__':  # Programmstart
    logic.setup()
    options = [task_1]

    print "Wähle den Task\n" \
          "0: Aufgabe 1 " \


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
