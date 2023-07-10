#!/usr/bin/python3
"""Defines AClass Rectangle Inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent Rectangle Using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return Area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str() of Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
