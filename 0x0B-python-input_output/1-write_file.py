#!/usr/bin/python3
"""
0. Read file

"""


def write_file(filename="", text=""):
    """A simple func to read a file """
    with open(filename, "w") as r:
        s = r.write(text)
        return(r.tell())
