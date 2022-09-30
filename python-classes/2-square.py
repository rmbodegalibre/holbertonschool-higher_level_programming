#!/usr/bin/python3
"""
This is class that define a square
"""


class Square:
    """Define constructor to init the class"""
    def __init__(self, size=0):
        self.__size = size

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                """ Defining private __size """
                self.__size = size
        else:
            raise TypeError("size must be an integer")
