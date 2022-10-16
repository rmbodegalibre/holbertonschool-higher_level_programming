#!/usr/bin/python3
"""
this module contains a function that appends a string at the end of
a text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    This function apoends a string at the end of a text file (UTF8)
    and returns the number of characters added
    * If file doesn't exist, it will be created.
    * It uses the with statement
    * It should create the file if doesn’t exist.
    * should overwrite the content of the file if it already exists.
    """
    with open(filename, "a", encoding="utf-8") as fName:
        fName.write(text)
    return len(text)
