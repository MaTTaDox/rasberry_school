
import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'abcD123')


def db():

    try:

        cur = con.cursor()

        cur.execute("SHOW DATABASES LIKE 'readings'")

        x = cur.fetchone()

        print vars(x)

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)


