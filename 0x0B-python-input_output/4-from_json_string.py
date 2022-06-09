#!/usr/bin/python3
"""
File: 4-from_json_string.py - Write a function that returns an object
(Python data structure) represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """
    from_json_string function Write a function that returns an object
    """
    return json.loads(my_str)
