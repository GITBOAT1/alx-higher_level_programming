#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def host():
    """ this is where my sql starts """
    MY_HOST = "localhost"

    db = MySQLdb.connect(host=MY_HOST, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    name = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = '{}'"
                "ORDER BY states.id ASC".format(name))

    for i in cur:
        """ print all the valuse in states """
        if (i[1] == name):
            print(i)

    """ close the data base """
    cur.close()
    db.close()


if __name__ == "__main__":
    host()
