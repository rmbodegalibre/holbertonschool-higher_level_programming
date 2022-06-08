#!/usr/bin/python3
"""
File: 3-is_kind_of_class.py (Write a function that returns True if the object
is an instance of, or if the object is an instance of a class that inherited
from, the specified class ; otherwise False.)
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class function (receive obj, and a_class)
    """
    return isinstance(obj, a_class)
    """
    isinstance: evaluate if obj is an instance of class
    """
