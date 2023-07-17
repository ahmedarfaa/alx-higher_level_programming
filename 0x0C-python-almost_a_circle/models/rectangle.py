#!/usr/bin/python3
"""Creating a new Class named Rectangle"""
from .base import Base


class Rectangle(Base):
    """Intializing the Rec class inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inializing the attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returning the value of the property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the value of the property"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Returning the value of the property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of the property"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Returning the value of the property"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value of the property"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Returning the value of the property"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the value of the property"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Defining anew method that retrives the area of rec"""
        return (self.__height * self.__width)

    def display(self):
        """Creating a method that draw a Rec in # shap"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """handleing str method"""
        return ("[{}] ({}) {}/{} - {}/{}"
                .format(str(self.__class__.__name__), self.id,
                        self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """updating the rec class with new args"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Defining anew method """
        obj_dictionary = {'id': self.id, 'height': self.height,
                          'width': self.width, 'x': self.x, 'y': self.y}
        return (obj_dictionary)
