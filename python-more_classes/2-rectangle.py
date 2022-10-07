#!/usr/bin/python3
"""
This program contains a class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)
"""


class Rectangle:
    """This class defines a rectangle by: (based on 0-rectangle.py)"""

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
