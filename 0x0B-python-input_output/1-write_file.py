#!/usr/bin/python3
"""
File: 1-write_file.py - Write a function that writes a string
to a text file (UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    write_file method writes a string to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        """
        Method open returns a file object
        """
        return f.write(text)
