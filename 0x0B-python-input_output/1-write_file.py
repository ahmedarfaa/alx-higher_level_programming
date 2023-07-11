#!/usr/bin/pyhton3
""" Defines a write_file-function  that write to afile"""


def write_file(filename="", text=""):
    """ writeing to afile and create it if it doesnot exits
    args:
        filename: ..
        text:..
        """
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
