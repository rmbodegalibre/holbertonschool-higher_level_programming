#!/usr/bin/python3
"""
File: models/base.py - the first class Base
"""


class Base:
    __nb_objects = 0
    """
    Private class attribute
    """
    def __init__(self, id=None):
        """ Instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects