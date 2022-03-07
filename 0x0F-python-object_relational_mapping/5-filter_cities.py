#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def host():
    """ this is where my sql starts """
    MY_HOST = "localhost"
    if len(sys.argv) == 5:
        db = MySQLdb.connect(host=MY_HOST, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        city = sys.argv[4]
        sq = ""
        cur.execute("SELECT cities.name FROM cities INNER JOIN "
                    "states ON states.id = cities.state_id"
                    " WHERE states.name = '%s'" % city)
        row = []
        for i in cur:
            """ store values in list """
            row.append(i[0])
        for j in range(len(row)):
            if j == (len(row)-1):
                print(row[j], end="")
            else:
                print(row[j], end=", ")
        print()

        """ close the data base """
        cur.close()
        db.close()


if __name__ == "__main__":
    host()
