#!/usr/bin/python
# -*- coding: utf-8 -*-

import src.logic as logic
import src.task_1 as task_1
import src.task_2 as task_2
import src.task_3 as task_3
import src.task_4 as task_4
import src.task_5 as task_5


if __name__ == '__main__':  # Programmstart
    logic.setup()
    options = [task_1, task_2, task_3, task_4, task_5]

    print "Wähle den Task:\n" \
          "0. Aufgabe 1\n" \
          "1. Aufgabe 2\n" \
          "2. Aufgabe 3\n" \
          "3. Aufgabe 4\n" \
          "4. Aufgabe 5\n"

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
