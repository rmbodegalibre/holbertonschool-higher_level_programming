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

        ------------------
        Update the class Rectangle by adding validation of all setter methods
        and instantiation (id excluded):

        """

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for heignt"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for heignt"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
