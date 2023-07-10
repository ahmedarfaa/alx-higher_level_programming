#!/usr/bin/python3
"""Defines AFunction which adds Attributes to objects."""


def add_attribute(obj, att, value):
    """Add new-attribute to Object if possible.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
