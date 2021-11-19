#!/usr/bin/python3
"""A simple scipt about avg"""
from sys import argv

if __name__ == '__main__':
    if (len(argv) == 1):
        print("{:d} argument.".format(1 - len(argv)))
    else:
        print("{:d} argument:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
