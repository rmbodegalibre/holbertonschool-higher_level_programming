#!/usr/bin/python3
"""
lookup: Return a list of available attributes and methods of the object
"""


def lookup(obj):
    return(obj.__dict__)
