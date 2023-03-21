#!/usr/bin/python3
"""
Rectangle that defines a rectangle by: (based on 0-rectangle.py)

"""


class Rectangle:
    """ An empty Rectangle """

    def __init__(self, width=0, height=0):
        """ instantiat width """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        return the value in width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if isinstance(value, (int)):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ return the value in width """
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for Height """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ Public instance method that returns the rectangle area """
        height = self.height
        weight = self.width
        return (height * weight)

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter """
        height = self.height
        weight = self.width
        if height == 0 or weight == 0:
            return (0)
        per = (height + weight)
        return (per * 2)

    def __str__(self):
        """prints rectangle"""
        if self.height == 0 or self.width == 0:
            return ''
        hashes = '#' * self.width
        return '\n'.join(hashes for i in range(self.height))

    def __repr__(self):
        """prints rectangle"""
        eval('Rectangle(self.width, self.height)')
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
