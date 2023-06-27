#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represent Square."""

    def __init__(self, size=0):
        """Initialize new Square.

        Args:
            size (int): size of new Square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set current Size of Square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of Square."""
        return (self.__size * self.__size)
