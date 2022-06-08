#!/usr/bin/python3
"""
File: 9-rectangle.py - Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializing class
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method area returns area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method __str__ defines description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
