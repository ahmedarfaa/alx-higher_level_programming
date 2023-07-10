#!/usr/bin/python3
"""Defines Aclass-checking-Function."""


def is_same_class(obj, a_class):
    """Check if An-Object is Exactly An-instance of a given class.

    Args:
        obj (any): The object to check.
    """
    if type(obj) == a_class:
        return True
    return False
