#!/usr/bin/python3
"""
Rectangle that defines a rectangle by: (based on 0-rectangle.py)

"""


class Rectangle:
    """ An empty Rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ instantiat width """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        hashes = "{}".format(self.print_symbol) * self.width
        return '\n'.join(hashes for i in range(self.height))

    def __repr__(self):
        """prints rectangle"""
        eval('Rectangle(self.width, self.height)')
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """compares two Rectangles
        Args
           rect_1
           rect_2
        Returns bigger rectangle or rect_1 if same
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
