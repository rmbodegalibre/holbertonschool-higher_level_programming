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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation of list_objs
        to a file:
        * list_objs is a list of instances who inherits of Base - example:
          list of Rectangle or list of Square instances
        * If list_objs is None, save an empty list
        * The filename must be: <Class name>.json - example: Rectangle.json
        * You must use the static method to_json_string (created before)
        * You must overwrite the file if it already exists
        """
        lst = []
        if list_objs is not None:
            for i in list_objs:
                lst.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(lst))
