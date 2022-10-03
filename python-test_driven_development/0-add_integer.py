#!/usr/bin/python3
"""
This file has a function to add two integers
"""


def add_integer(a, b=98):
    """This function receives two values, this function evaluates
    if both values are integers or float type."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
        return
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
        return
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
