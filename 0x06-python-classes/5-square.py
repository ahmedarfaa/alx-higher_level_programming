#!/usr/bin/python3
"""Define a Class square."""


class Square:
    """Represent a Square."""

    def __init__(self, size):
        """Initialize new Square.

        Args:
            size (int): Size of new Square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set THE current size of Square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return Current Area of Square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print Square with  # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
