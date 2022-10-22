#!/usr/bin/python3
"""
This module contains the class Rectangle that inherits of Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits of Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Call the super class with id - this super call with use
        the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        """
        Private instance attributes, each with its own public getter and setter
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        """

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.__width = value

    @property
    def height(self):
        """getter for width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for width"""
        self.__height = value

    @property
    def x(self):
        """getter for width"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for width"""
        self.__x = value

    @property
    def y(self):
        """getter for width"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for width"""
        self.__y = value
