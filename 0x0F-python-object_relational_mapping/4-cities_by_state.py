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
        cy_st = ""
        sq = ""
        cur.execute("SELECT cities.id, cities.name, states.name"
                    " FROM cities INNER JOIN states ON "
                    "states.id = cities.state_id ORDER BY cities.id ASC")
        for i in cur:
            """ print all the valuse in states """
            print(i)

        """ close the data base """
        cur.close()
        db.close()
    else:
        print("Usage:./0-select_states.py username,password and database name")


if __name__ == "__main__":
    host()
