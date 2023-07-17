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
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returning the property value"""
        return self.__width

    @size.setter
    def size(self, value):
        """setting the property value"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value
        self.__width = value

    def __str__(self):
        """handleing __str__ method"""
        return ("[{}] ({}) {}/{} - {}".format(str(self.__class__.__name__),
                self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Updateing the Square class"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Defining anew method """
        obj_dictionary = {'id': self.id,
                          'size': self.size, 'x': self.x, 'y': self.y}
        return (obj_dictionary)
