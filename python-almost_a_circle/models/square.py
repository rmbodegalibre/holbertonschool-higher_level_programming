#!/usr/bin/python3
"""
This module contains the class Square that inherits of Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height
        - this super call will use the logic of the __init__ of
        the Rectangle class. The width and height must be assigned
        to the value of size
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overriding the __str__ method so that it returns:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.height

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """
        public method that returns the dictionary representation of a Rectangle
        This dictionary must contain:
        * id
        * width
        * height
        * x
        * y
        """
        dictio = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y}
        return dictio
 