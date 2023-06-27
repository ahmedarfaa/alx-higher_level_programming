#!/usr/bin/python3
"""define a class square."""


class Square:
    """represent square."""

    def __init__(self, size=0):
        """initialize the new Square.

        Args:
            size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/Set Current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return Current Area of square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """define the == Comparision to square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """define the != Comparison to square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """define the < Comparison to square."""
        return self.area() < other.area()

    def __le__(self, other):
        """define the < or = Comparison to square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define the > comparison to square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """define the > or = Compmarison to square."""
        return self.area() >= other.area()
