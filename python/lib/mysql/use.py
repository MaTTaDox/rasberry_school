
import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'abcD123', 'readings')


def execute(query):

    try:

        cur = con.cursor()

        cur.execute(query)

        return cur

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)


