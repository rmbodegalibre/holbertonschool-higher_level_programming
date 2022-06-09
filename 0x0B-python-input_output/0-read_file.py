#!/usr/bin/python3
"""
File: 0-read_file.py - Write a function that reads a text file (UTF8)
and prints it to stdout:
"""


def read_file(filename=""):
    """
    read_file function is defined below
    """
    with open(filename, encoding="utf-8") as f:
        """
        Method open returns returns a file object
        """
        print(f.read(), end="")
