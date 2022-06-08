#!/usr/bin/python3
"""
File: 101-add_attribute.py - function that adds new attribute
to an object if it’s possible:
"""


def add_attribute(obj, a, v):
    """
    add_attribute function is defined below
    """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
        """ setattr adds new attribute """
    else:
        raise TypeError("can't add new attribute")
        """
        If this isn't possible, raise an error
        """
