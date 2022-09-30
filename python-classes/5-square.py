#!/usr/bin/python3
"""
Square: Define a class to build a square
"""


class Square:
    """ Initializing an instance of class square  """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ Return the size of the square """
        return (self.__size)

    @size.setter
    def size(self, val):
        """ Property by which the size is defined """
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """ Returns the result of squaring size. """
        return (self.__size ** 2)

    def my_print(self):
        """
        Printing a square filled with the character "#"
        """
        if not self.__size:
            print()
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print()
