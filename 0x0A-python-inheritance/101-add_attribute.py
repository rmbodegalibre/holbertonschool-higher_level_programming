#!/usr/bin/python3
"""
File: 101-add_attribute.py - function that adds new attribute
to an object if it’s possible:
"""


def add_attribute(obj, a, v):
    """
    add_attribute function is defined below
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
        """
        If this has attribute, raise an error
        """
    else:
        setattr(obj, a, v)
        """ setattr adds new attribute """
