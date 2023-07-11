#!/usr/bin/python3
"""Define a function that returns  the json represntation"""
import json


def to_json_string(my_obj):
    """ Returning JSON repersentaion"""
    return json.dumps(my_obj)
