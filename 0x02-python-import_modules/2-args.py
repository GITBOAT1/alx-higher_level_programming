#!/usr/bin/python3
"""A simple scipt about avg"""
from sys import argv

if __name__ == '__main__':
    print("{} arguments:".format(len(argv)))

    for i in range(1, len(argv)):
        print("{}".format(argv[i]))
