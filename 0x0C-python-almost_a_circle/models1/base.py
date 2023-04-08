#!/usr/bin/python3
"""
 first class Base
"""


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ first class method """
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
