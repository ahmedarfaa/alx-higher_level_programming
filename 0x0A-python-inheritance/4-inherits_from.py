#!/usr/bin/python3
"""Defines An-Inherited class-checking-Function."""


def inherits_from(obj, a_class):
    """Check If An-Object is An-inherited instance of a class.

    Args:
        obj (any): The object to check.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
