#!/usr/bin/python3
"""
This file contains a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding = "utf-8") as fName:
        read_data = fName.read()
    print(read_data, end="")
