#!/usr/bin/python3
"""Defines A-Rectangle Subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent ASquare."""i

    def __init__(self, size):
        """Initialize a new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return Area of square."""
        return self.__size* self.__size

    def __str__(self):
        """Return print() and str() of Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
