#!/usr/bin/python3
"""
lookup: Return a list of available attributes and methods of the object
"""


class MyList(list):
    """
    Method print_sorted prints the list in order
    """
    def print_sorted(self):
        print(sorted(self))
