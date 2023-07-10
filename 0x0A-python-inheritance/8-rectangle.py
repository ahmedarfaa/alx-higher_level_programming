#!/usr/bin/python3
"""Defines AClass-Rectangle inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent A-Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize A-new_Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
