#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def host():
    """ this is where my sql starts """
    if len(sys.argv) == 5:
        MY_HOST = "localhost"

        db = MySQLdb.connect(ho-st=MY_HOST, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        name = sys.argv[4]
        s = "SELECT * FROM states WHERE name = '%s'  ORDER BY states.id ASC"
        cur.execute(s % name)

        for i in cur.fetchall():
            """ print all the valuse in states """
            print(i)

            """ close the data base """
        cur.close()
        db.close()


if __name__ == "__main__":
    host()
