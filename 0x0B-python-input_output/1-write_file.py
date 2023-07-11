#!/usr/bin/pyhton3
""" Defines afunction  that write to afile"""


def write_file(filename="", text=""):
    """ writeing to afile and create it if it doesnot exits"""
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
