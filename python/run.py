#!/usr/bin/python
# -*- coding: utf-8 -*-
import lib.MFRC522 as MFRC522
import signal
import redis

continue_reading = True

if __name__ == '__main__':

    try:
        print 'Programm mit CTRL-C beenden.'

        # Capture SIGINT for cleanup when the script is aborted
        def end_read(signal, frame):
            global continue_reading
            print "Ctrl+C captured, ending read."
            continue_reading = False

        signal.signal(signal.SIGINT, end_read)

        MIFAREReader = MFRC522.MFRC522()

        r = redis.StrictRedis(host='localhost', port=6379, db=0)

        # Welcome message
        print "Welcome to the MFRC522 data read example"
        print "Press Ctrl-C to stop."

        # This loop keeps checking for chips. If one is near it will get the UID and authenticate
        while continue_reading:

            # Scan for cards
            (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            # If a card is found
            if status == MIFAREReader.MI_OK:
                print "Card detected"

            # Get the UID of the card
            (status, uid) = MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == MIFAREReader.MI_OK:

                uidStr = str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])

                # Print UID
                print "Card read UID: " + uidStr

                # This is the default key for authentication
                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                # Select the scanned tag
                MIFAREReader.MFRC522_SelectTag(uid)

                # Authenticate
                status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

                # Check if authenticated
                if status == MIFAREReader.MI_OK:

                    r.set('rfid_'+ uidStr, True, 10)

                    r.publish('rfid_authentication', uidStr)

                    MIFAREReader.MFRC522_Read(8)
                    MIFAREReader.MFRC522_StopCrypto1()
                else:
                    print "Authentication error"

    except KeyboardInterrupt:  # wenn 'CTRL-C' gedrückt, dann Ende
        print "Programm wird beendet"

