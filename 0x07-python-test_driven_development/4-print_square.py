#!/usr/bin/python3
"""

 a function that prints My name is <first name> <last name>

"""

msg1 = "size must be an integer"
msg2 = "size must be >= 0"


def print_square(size):
    """ a function that prints a square with the character #. """
    if not isinstance(size, (int, float)):
        raise TypeError(msg1)
    if size < 0:
        raise ValueError(msg2)
    s1 = size
    for i in range(size):
        for row in range(size):
            if row != s1 - 1:
                print("#", end="")
            else:
                print("#")
