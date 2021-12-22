#!/usr/bin/python3
"""
0. Read file

"""


def read_file(filename=""):
    """A simple func to read a file """
    with open(filename, "r") as r:
        s = r.read()
    for i in s:
        print(i, end="")
