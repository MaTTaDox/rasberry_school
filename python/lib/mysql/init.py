
import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'abcD123')


def db():

    try:

        cur = con.cursor()

        cur.execute("SHOW DATABASES LIKE 'readings'")

        result = cur.fetchone()

        if result is None:
            cur.execute("CREATE DATABASE readings")
            cur.execute("USE readings")

            cur.execute("CREATE TABLE `locations` (`id` int(11) unsigned NOT NULL AUTO_INCREMENT, `identifer` varchar(200) NOT NULL DEFAULT '',PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;")

            cur.execute(
                "CREATE TABLE `values` ("
                "`id` int(11) unsigned NOT NULL AUTO_INCREMENT,"
                "`location_id` int(10) unsigned NOT NULL,"
                "`datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
                "PRIMARY KEY (`id`),"
                "KEY `location_id` (`location_id`),"
                "CONSTRAINT `values_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE CASCADE ON UPDATE CASCADE"
                ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
            )
    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)


