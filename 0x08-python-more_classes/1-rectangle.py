#!/usr/bin/python3
"""
an empty class Rectangle that defines a rectangle

"""


class Rectangle:
    """ An empty Rectangle """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """ return the value in width """
        return(self.width)

    @width.setter
    def width(self, value):
        """setter for width """
        if isinstance(value, (int)):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ return the value in width """
        return(self.height)

    @height.setter
    def height(self, value):
        """setter for Height """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value
        else:
            raise TypeError("width must be an integer")
