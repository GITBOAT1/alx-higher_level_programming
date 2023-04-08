#!/usr/bin/python3

'''
Defines the class Rectangle
'''
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor, initialize the private vales """
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width of Rectangle """
        return self.__wdidth

    @property
    def height(self):
        """ width of Rectangle """
        return self.__hight

    @property
    def x(self):
        """ x of Rectangle """
        return self.__x

    @property
    def y(self):
        """ y of Rectangle """
        return self.__y

    @width.setter
    def widht(self, width):
        """ set the values """
        self.__width = width

    @height.setter
    def height(self, height):
        """ set the values """
        self.__height = height

    @x.setter
    def x(self, x):
        """ set the values """
        self.__x = x

    @y.setter
    def y(self, y):
        """ set the values """
        self.__y = y
