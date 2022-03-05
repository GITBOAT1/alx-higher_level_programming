#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def host():
    """ this is where my sql starts """
    MY_HOST = "localhost"
    if len(sys.argv) == 4:
        db = MySQLdb.connect(host=MY_HOST, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()

        cur.execute("SELECT * FROM states")

        for i in cur:
            """ print all the valuse in states """
            if i[1][0] == "N":
                print(i)

        """ close the data base """
        cur.close()
        db.close()
    else:
        print("Usage:./0-select_states.py username,password and database name")


if __name__ == "__main__":
    host()
