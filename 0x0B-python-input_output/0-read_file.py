#!/usr/bin/pyhton3
"""Define afunction that reads afile"""


def read_file(filename=""):
    """Read_file function"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
