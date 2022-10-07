#!/usr/bin/python3
"""
This program contains a class Rectangle that defines a rectangle by:
(based on 4-rectangle.py)
"""


class Rectangle:
    """This class defines a rectangle by: (based on 4-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """Initializing the class Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width of Rectangle"""
        return self.__width

    @property
    def height(self):
        """Get the height of Rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width Property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height Property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This function returns the area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """This function returns the perimeter of Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """This function prints a rectangle filled with char # """
        pict = ""
        if self.__height == 0 or self.width == 0:
            return pict
        for i in range(self.__height):
            pict += ("#" * self.__width)
            if i is not self.__height - 1:
                pict += "\n"
        return pict

    def __repr__(self):
        """This function show the formal representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when this instance of Rectangle is deleted."""
        print("Bye rectangle...")
