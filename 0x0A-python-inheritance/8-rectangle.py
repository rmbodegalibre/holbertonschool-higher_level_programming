#!/usr/bin/python3
"""
File: 8-rectangle.py - Write a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class is defined below
    """
    def __init__(self, width, height):
        """ Instantiation this class """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
