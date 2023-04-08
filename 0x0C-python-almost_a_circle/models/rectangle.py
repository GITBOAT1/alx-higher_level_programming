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
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @height.setter
    def height(self, height):
        """ set the values
        """
        heitht
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @x.setter
    def x(self, x):
        """ set the values
        """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be > 0')
        self.__x = x

    @y.setter
    def y(self, y):
        """ set the values
        """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be > 0')
        self.__y = y

    def area(self):
        """returns area of rectangle"""
        return (self.height * self.width)

    def display(self):
        """displays rectangle"""
        print('\n' * self.y, end="")
        for i in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """returns string of info about rectangle"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        if args:
            keys = ['id', 'width', 'height', 'x', 'y']
            for k, v in zip(keys, args):
                setattr(self, k, v)
        else:
            keys = ['id', 'width', 'height', 'x', 'y']
            if kwargs is not None:
                for k, v in kwargs.items():
                    if k in keys:
                        setattr(self, k, v)

    def to_dictionary(self):
        """dictiobnary representation of rectangle"""
        my_dic = {}
        keys = ['id', 'width', 'height', 'x', 'y']

        for k in keys:
            my_dic[k] = getattr(self, k)
        return (my_dic)
