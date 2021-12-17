#!/usr/bin/python3
"""
Prototype: def add_integer(a, b=98):

    a function that adds 2 integers.
"""

Err = " must be an interger"


def add_integer(a, b=98):
    """
    This is the "example" module.
    """

    test = 0
    if isinstance(a, (int, float)):
        test = 3
    if isinstance(b, (int, float)):
        test = test + 2
    if test == 5:
        return (int(a) + int(b))
    elif test == 3:
        raise TypeError('b' + Err)
    elif test == 2:
        raise TypeError('a' + Err)
    elif a == None:
        raise TypeError('a' + Err)
