#!/usr/bin/python3
"""
File: 9-student.py - Write a class Student that defines a student by
"""


class Student:
    """
    class that represents a student
    """
    def __init__(self, first_name, last_name, age):
        """ Instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attribs=None):
        """
        to_json - retrieves a dictionary representation of a Student instance
        """
        if attribs is None:
            return self.__dict__
        else:
            dictio = dict()
            for idx in attribs:
                if idx in self.__dict__:
                    dictio[idx] = self.__dict__[idx]
            return dictio
