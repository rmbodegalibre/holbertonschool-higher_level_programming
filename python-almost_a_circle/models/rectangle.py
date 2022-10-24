#!/usr/bin/python3
"""
This module contains the class Rectangle that inherits of Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits of Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Call the super class with id - this super call with use
        the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        """
        Private instance attributes, each with its own public getter and setter
        __width -> width
        __height -> height
        __x -> x
        __y -> y

        ------------------
        Update the class Rectangle by adding validation of all setter methods
        and instantiation (id excluded):

        """

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns the area value of Rectangle instance."""
        return self.width * self.height

    def display(self):
        """
        public method def display(self): that prints in stdout the
        Rectangle instance with the character #
        ---
        Update: rint in stdout the Rectangle instance
        with the character # by taking care of x and y
        """
        for down in range(self.__y):
            print()

        for i in range(self.__height):
            for right in range(self.__x):
                print(" ", end="")

            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """
        Overriding the __str__ method so that it returns:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.height)

    def update(self, *args, **kwargs):
        """
        def update(self, *args):
        Public method that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        This type of argument is called a “no-keyword argument”
        - Argument order is super important.
        ---
        Updating the public method by changing the prototype to
        update(self, *args, **kwargs) that assigns a key/value argument
        to attributes

        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.__width = kwargs["width"]
        if "height" in kwargs:
            self.__height = kwargs["height"]
        if "x" in kwargs:
            self.__x = kwargs["x"]
        if "y" in kwargs:
            self.__y = kwargs["y"]

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
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y}
        return dictio
