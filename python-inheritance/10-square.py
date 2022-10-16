#!/usr/bin/python3
"""
File: 10-square.py - class Square inherits from Rectangle (9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class is defined below
    """
    def __init__(self, size):
        """ Instantiation """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
