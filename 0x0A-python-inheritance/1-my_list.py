#!/usr/bin/python3
"""
File: 1-my_list.py (Write a class MyList that inherits from list:)
"""


class MyList(list):
    """
    My list class inherits from list
    """
    def print_sorted(self):
        """
        Method print_sorted prints the list in order
        """
        print(sorted(self))
