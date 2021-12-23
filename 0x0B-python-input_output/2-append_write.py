#!/usr/bin/python3
"""
0. append file

"""


def append_write(filename="", text=""):
    """A simple func to read a file """
    with open(filename, "a") as r:
        s = r.write(text)
        return(r.tell())
