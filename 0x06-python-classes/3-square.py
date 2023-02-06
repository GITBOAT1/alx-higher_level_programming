#!/usr/bin/python3
"""Square with size"""


class Square:
    """ The size of a square is crucial for a square, many things depend of it
    """
    __size = None

    def __init__(self, size=0):
        """ init method """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
