#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    f_char = sentence[0] if length > 0 else "None"
    tup = length, f_char
    return(tup)
