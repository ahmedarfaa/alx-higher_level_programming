#!/usr/bin/python3
"""Defines AN-inherited list Class MyList."""


class MyList(list):
    """Implements sorted printing for built-in list class."""

    def print_sorted(self):
        """Print Alist sorted ascending order."""
        print(sorted(self))
