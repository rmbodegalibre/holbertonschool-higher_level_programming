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
        """ Setting size of the square """
        return (self.__size)
        """ property to retrieve size """

    @size.setter
    def size(self, size):
        """ Size property to set size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the calculation of the area of a square """
        return (self.__size * self.__size)

    def my_print(self):
        """ printing a square filled with #
        """
        if not self.__size:
            print()
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print()
