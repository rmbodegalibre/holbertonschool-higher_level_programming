#!/usr/bin/python3
"""
File: 7-base_geometry.py - Write a class BaseGeometry
(based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    BaseGeometry class is defined below
    """
    def area(self):
        """
        area is a public instance method
        """
        raise Exception("area() is not implemented")
        """
        It raises an Exception with the message
        area() is not implemented
        """

    def integer_validator(self, name, value):
        """
        integer_validator function validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
