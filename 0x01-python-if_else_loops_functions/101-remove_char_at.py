#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for x, y in enumerate(str):
        if x != n:
            newstr += y
    return newstr
