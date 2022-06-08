#!/usr/bin/python3
"""
File: 4-inherits_from.py (Write a function that returns True if the object
is an instance of a class that inherited (directly or indirectly) from the
specified class ; otherwise False.)
"""


def inherits_from(obj, a_class):
    """
    inherits_from function (receive obj, and a_class)
    """
    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False
    """
    issubclass funcion evaluates if obj is an instance of a class
    that inherited (directly or indirectly) from the specified class
    """
