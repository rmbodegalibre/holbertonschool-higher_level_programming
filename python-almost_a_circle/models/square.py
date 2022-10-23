#!/usr/bin/python3
"""
This module contains the class Square that inherits of Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height
        - this super call will use the logic of the __init__ of
        the Rectangle class. The width and height must be assigned
        to the value of size
        """
        super().__init__(size, size, x, y, id)
