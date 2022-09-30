#!/usr/bin/python3
"""
Square: Define a class to build a square
"""


class Square:
    """ Initializing an instance of class square  """
    def __init__(self, size=0):
        self.size = size

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                """ Defining private instance __size """
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns the result of squaring size. """
        return (self.__size ** 2)


