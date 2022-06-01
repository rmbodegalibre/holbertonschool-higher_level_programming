#!/usr/bin/python3
"""
Rectangle: Define a class to build a rectangle
"""


class Rectangle:
    number_of_instances = 0
    """ Initializing an instance of class rectangle  """
    def __init__(self, width=0, height=0):
        """ Defining size like private instance """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ("")

        hashtag = []
        for i in range(self.__height):
            [hashtag.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                hashtag.append("\n")
        return ("".join(hashtag))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        hashtag = "Rectangle(" + str(self.__width)
        hashtag += ", " + str(self.__height) + ")"
        return (hashtag)

    def __del__(self):
        """Print a message when an instance of rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
