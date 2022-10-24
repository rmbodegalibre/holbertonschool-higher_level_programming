#!/usr/bin/python3
"""
This module contains the first class Base:
"""
import json


class Base:
    """
    This is the first class Base: The goal of it is to manage
    id attribute in all the future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        Instanciation
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation
        of list_dictionaries
        * list_dictionaries is a list of dictionaries
        * If list_dictionaries is None or empty, return the string: "[]"
        * Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))
