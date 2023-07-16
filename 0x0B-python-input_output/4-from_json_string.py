#!/usr/bin/python3
"""Define afunction that return object from json repr"""
import json


def from_json_string(my_str):
    """Retrun object repersented in json"""
    return json.loads(my_str)
