#!/usr/bin/python3
"""
File: models/base.py - the first class Base
"""


class Base:
    """
    Base Class to define numbres of objects
    """
    __nb_objects = 0
    """
    Private class attribute
    """
    def __init__(self, id=None):
        """ Instantiation for set values """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
