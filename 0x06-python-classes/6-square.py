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

    @property
    def size(self):
        """ property get to retrieve it """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ property setter to set """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """gets position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position
        Args:
            value: value of position
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """prints square offsetting it by position with symbol #"""
        if self.size == 0:
            print('')
            return
        for i in range(self.__position[1]):
            print('')
        for i in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], '#' * self.__size))
