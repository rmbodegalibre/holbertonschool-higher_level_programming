#!/usr/bin/python3
"""
File: 2-append_write.py - Write a function that appends a string at the end
of a text file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    append_write method appends a string at the end of a text file (UTF8)
    """
    with open(filename, 'a') as f:
        app = f.write(text)
    return app
