#!/usr/bin/python3
"""
File: 11-square.py - class Square inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class is defined below
    """
    def __init__(self, size):
        """ Instatiation """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ Str Method returns the print and str"""
        return "[Square] {}/{}".format(self.__size, self.__size)
