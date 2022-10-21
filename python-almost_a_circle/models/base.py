#!/usr/bin/python3
"""
This module contains the first class Base:
"""


class Base:
    """
    This is the first class Base: The goal of it is to manage
    id attribute in all the future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        Instanciation
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
