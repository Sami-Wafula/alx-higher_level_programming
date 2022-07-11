#!/usr/bin/python3
""" Base class for other classes in 0x0C-python-almost_a_circle"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ instatiate Base class object"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
