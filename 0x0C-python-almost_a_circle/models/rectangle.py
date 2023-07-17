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
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}/{}"
                .format(str(self.__class__.__name__), self.id,
                        self.__x, self.__y, self.__width, self.__height))
