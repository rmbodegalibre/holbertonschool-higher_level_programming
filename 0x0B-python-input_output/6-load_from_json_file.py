#!/usr/bin/python3
"""
File: 6-load_from_json_file.py - Write a function that creates an Object
from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file function Write a function that creates an Object
    from a “JSON file”
    """
    with open(filename) as f:
        return json.load(f)
