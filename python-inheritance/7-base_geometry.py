#!/usr/bin/python3
"""
This module contains a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry():
    """
    It's a class BaseGeometry.
    """
    def area(self):
        """
        It's a public instance method that raises an exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        It's a public instance method that validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
