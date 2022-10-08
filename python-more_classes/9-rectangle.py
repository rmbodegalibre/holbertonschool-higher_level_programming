#!/usr/bin/python3
"""
This program contains a class Rectangle that defines a rectangle by:
(based on 7-rectangle.py)
"""


class Rectangle:
    """This class defines a rectangle by: (based on 7-rectangle.py)"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the class Rectangle, add 1 instance to the counter"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            pict += (str(self.print_symbol) * self.__width)
            if i is not self.__height - 1:
                pict += "\n"
        return pict

    def __repr__(self):
        """This function show the formal representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when this instance of Rectangle is deleted.
        decreases 1 instance in the counter
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        This method returns a new rectangle instance with
        width == height == size
        Args:
            cls: Type[Self@Rectangle]
            size: Int
        """
        return Rectangle(size, size)
