#!/usr/bin/python3
"""
File: 8-class_to_json.py - Write a function that returns the dictionary
description with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    class_to_json(obj) - returns the dictionary description with simple
    data structure
    """
    return obj.__dict__
