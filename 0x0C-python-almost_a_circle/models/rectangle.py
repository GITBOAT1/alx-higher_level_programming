#!/usr/bin/python3

'''
Defines the class Rectangle
'''
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor, initialize the private vales
        Args
           width
           height
           x
           y
           id - from Base class
        """
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width of Rectangle
        """
        return self.__width

    @property
    def height(self):
        """ width of Rectangle
        """
        return self.__height

    @property
    def x(self):
        """ x of Rectangle """
        return self.__x

    @property
    def y(self):
        """ y of Rectangle
        """
        return self.__y

    @width.setter
    def width(self, width):
        """ set the values
        """
        if not isinstance(width, int):
            raise TypeError('{} must be an integer'.format('width'))
        if width <= 0:
            raise ValueError('{} must be > 0'.format('width'))
        self.__width = width

    @height.setter
    def height(self, height):
        """ set the values
        """
        if not isinstance(height, int):
            raise TypeError('{} must be an integer'.format('height'))
        if height <= 0:
            raise ValueError('{} must be > 0'.format('height'))
        self.__height = height

    @x.setter
    def x(self, x):
        """ set the values
        """
        if not isinstance(x, int):
            raise TypeError('{} must be an integer'.format('x'))
        if x < 0:
            raise ValueError('{} must be > 0'.format('x'))
        self.__x = x

    @y.setter
    def y(self, y):
        """ set the values
        """
        if not isinstance(y, int):
            raise TypeError('{} must be an integer'.format('y'))
        if y < 0:
            raise ValueError('{} must be > 0'.format('y'))
        self.__y = y
