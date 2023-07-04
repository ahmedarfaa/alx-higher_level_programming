#!/usr/bin/python3
"""Defines  Alocked_Class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    """

    __slots__ = ["first_name"]
