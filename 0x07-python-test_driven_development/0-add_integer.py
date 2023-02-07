#!/usr/bin/python3
"""
Prototype: def add_integer(a, b=98):
    a function that adds 2 integers.
"""


def add_integer(a=0, b=98):
    """
    This is the "example" module.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
