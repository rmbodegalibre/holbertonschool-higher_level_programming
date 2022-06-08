#!/usr/bin/python3
"""
File: 100-my_int.py - Write a class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt class is defined below
    """
    def __eq__(self, other):
        """
        Return: True if equal
        """
        return self - other != 0

    def __ne__(self, other):
        """
        Return: True if not equal
        """
        return self - other == 0
