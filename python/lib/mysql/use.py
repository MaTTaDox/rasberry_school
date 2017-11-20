
import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'abcD123', 'rfid')


def execute(query):

    try:

        cur = con.cursor()
        cur.execute(query)
        con.commit()

        return cur

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)


