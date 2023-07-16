#!/usr/bin/python3
"""Defines aclass Student"""


class Student:
    """ Student class"""
    def __init__(self, first_name, last_name, age):
        """ Initalizing the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the class of all attributes"""
        return self.__dict__
