#!/usr/bin/python3
"""
This program contains a function that returns True if the object is exactly
an instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly an instance
    of the specified class; otherwise False.
    """
    return type(obj) == a_class
