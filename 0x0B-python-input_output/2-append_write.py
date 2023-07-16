#!/usr/bin/python3
"""Defines a function that appends text to afile"""


def append_write(filename="", text=""):
    """Appending text to afile
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
