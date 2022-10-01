#!/usr/bin/python3
"""
Square: Define a class to build a square
"""


class Square:
    """ Initializing an instance of class square  """
    def __init__(self, size=0, pos=(0, 0)):
        """Initializing new sqare"""
        self.size = size
        self.pos = pos

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

    @property
    def pos(self):
        """
        Property to get current position
        """
        return (self.__pos)

    @pos.setter
    def pos(self, val):
        """ Method position to set self.__position with value
        Args:
            value (int): value to set the self.__position variable
        """
    @pos.setter
    def pos(self, val):
        if (not isinstance(val, tuple) or
                len(val) != 2 or
                not all(isinstance(num, int) for num in val) or
                not all(num >= 0 for num in val)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__pos = val

    def area(self):
        """
        Returns the result of squaring size.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__pos[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__pos[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
