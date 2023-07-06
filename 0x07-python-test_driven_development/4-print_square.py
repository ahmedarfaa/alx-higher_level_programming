#!/usr/bin/python3
"""Defines Square_Printing function."""


def print_square(size):
    """Print a square with the # character.
    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is integer.
        ValueError: size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for j in range(size)]
        print("")
