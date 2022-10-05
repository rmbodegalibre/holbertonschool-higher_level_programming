#!/usr/bin/python3
"""
4-print_square.py
This program prints a square with the character #.
"""


def print_square(size):
    """
    This function prints a square with the character #.
    size is the size length of the square
    size must be an integer,
    otherwise raise a TypeError exception with the message:
    "size must be an integer"
    if size is less than 0,
    raise a ValueError exception with the message:
    "size must be >= 0"
    if size is a float and is less than 0,
    raise a TypeError exception with the message:
    "size must be an integer"
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
        return

    if size < 0:
        raise ValueError("size must be >= 0")
        return

    for i in range(0, size):
        print("#" * int(size))
