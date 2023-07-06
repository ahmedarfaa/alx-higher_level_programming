#!/usr/bin/python3
"""Defines Text_Indentation function."""


def text_indentation(text):
    """Print text with two lines after each '?', ':', and '.'.
    Args:
        text (string): The text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    z = 0
    while z < len(text) and text[z] == ' ':
        z += 1

    while z < len(text):
        print(text[z], end="")
        if text[z] == "\n" or text[z] in ".?:":
            if text[z] in ".?:":
                print("\n")
            z += 1
            while z < len(text) and text[z] == ' ':
                z += 1
            continue
        z += 1
