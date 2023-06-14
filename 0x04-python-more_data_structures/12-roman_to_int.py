#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    tot = 0
    Num = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in reversed(roman_string):
        Num = digits[x]
        tot += Num if tot < Num * 5 else -Num
    return tot
