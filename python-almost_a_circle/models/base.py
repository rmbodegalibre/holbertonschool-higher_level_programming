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

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON string
        representation json_string
        * json_string is a string representing a list of dictionaries
        * If json_string is None or empty, return an empty list
        * Otherwise, return the list represented by json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method def create(cls, **dictionary): that returns an instance
        with all attributes already set:

        **dictionary can be thought of as a double pointer to a dictionary
        - To use the update method to assign all attributes,
          you must create a “dummy” instance before:
        - Create a Rectangle or Square instance with “dummy” mandatory
          attributes (width, height, size, etc.)
        - Call update instance method to this “dummy” instance to apply your
          real values
        - You must use the method def update(self, *args, **kwargs)
        **dictionary must be used as **kwargs of the method update
        You are not allowed to use eval
        """
        if cls.__name__ == "Square":
            dummy = cls(8)
        elif cls.__name__ == "Rectangle":
            dummy = cls(4, 6)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances:

        * The filename must be: <Class name>.json - example: Rectangle.json
        * If the file doesn’t exist, return an empty list
        * Otherwise, return a list of instances - the type of these instances depends on cls (current class using this method)
        * You must use the from_json_string and create methods (implemented previously)
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_dics = cls.from_json_string(f.read())
                lst = []
                for i in list_dics:
                    lst.append(cls.create(**i))
                return lst
        except:
            return []
