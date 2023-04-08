#!/bin/python3

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class """
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
