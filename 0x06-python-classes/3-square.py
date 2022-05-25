#!/usr/bin/python3
"""
Square: Define a class to build a square
"""


class Square:
    """ Initializing an instance of class square  """
    def __init__(self, size=0):

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                """ Defining size like private instance """
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Return the calculation of the area of a square """
        return (self.__size * self.__size)
