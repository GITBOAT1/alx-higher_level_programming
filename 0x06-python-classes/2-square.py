#!/usr/bin/python3
"""Square with size"""


class Square:
    """ The size of a square is crucial for a square, many things depend of it
    (area computation, etc.), so you, as class builder, must control the type
    and value of this attribute. One way to have the control is to keep it
    privately. You will see in next tasks how to get, update and validate the
    size value.

    Args:
        size: this tells the size of the figure

    Attributes:
        size: Human readable string describing the exception.
    """
    __size = None

    def __init__(self):
        """ init method """
        self.__size = None
