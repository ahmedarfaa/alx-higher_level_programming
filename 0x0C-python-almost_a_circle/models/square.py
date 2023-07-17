#!/usr/bin/python3
"""Creating anew Class called Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """inializing the Square class that inherits from Rec class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inializing the class attributes"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y)

    @property
    def size(self):
        """Returning the property value"""
        return self.__width

    @size.setter
    def size(self, value):
        """setting the property value"""
        if (type(value) is not int):
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value
        self.__width = value

    def __str__(self):
        """handleing __str__ method"""
        return (" [{}] ({}) {}/{} - {}".format(str(self.__class__.__name__),
                self.id, self.x, self.y, self.__width))
