#!/usr/bin/python3
"""define A  magic-class Matching Exactly bytecode Provided by >> Holberton."""

import math


class MagicClass:
    """Rrpresent A  Circle."""

    def __init__(self, radius=0):
        """initialize a magic-class.

        Arg:
            radius (float or int): Radius of the new magic-class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return Area of magic-class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return the Circumference of magic-class."""
        return (2 * math.pi * self.__radius)
