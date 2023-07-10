#!/usr/bin/python3
"""Defines Aclass && inherited class-Checking-Function."""


def is_kind_of_class(obj, a_class):
    """Check if An-Object is An-Instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
    """
    if isinstance(obj, a_class):
        return True
    return False
