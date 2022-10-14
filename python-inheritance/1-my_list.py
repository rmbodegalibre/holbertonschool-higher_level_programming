#!/usr/bin/python3
"""
This program contains a class MyList that inherits from list:
"""


class MyList(list):
    """It's a subclass from list class"""
    def print_sorted(self):
        """This function prints a list yn sorted order"""
        print(sorted(self))
