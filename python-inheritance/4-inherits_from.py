#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an
instance of a class that inherited (directly or indirectly)
of the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    This function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    of the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
