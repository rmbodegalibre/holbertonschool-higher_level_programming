#!/usr/bin/python3
"""
This module contains a function that creates an Object of one “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    This function creates an Object of one “JSON file”
    """
    with open(filename, encoding="utf-8") as fName:
        txt = fName.read()
        return json.loads(txt)
