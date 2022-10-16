#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    This function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    * It uses the with statement
    * It should create the file if doesn’t exist.
    * should overwrite the content of the file if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as fName:
        fName.write(text)
    return len(text)
