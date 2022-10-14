#!/usr/bin/python3
"""
This program contains a class MyList that inherits from list:
"""


class MyList(list):
    """It's a subclass of list class"""
    def print_sorted(self):
        """This function prints a list in sorted order"""
        print(sorted(self))
