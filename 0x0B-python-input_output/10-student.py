#!/usr/bin/python3
"""student class"""


class Student:
    """repr a student"""
    def __init__(self, first_name, last_name, age):
        """initialises new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets json version of student"""
        if type(attrs) == list and all(type(el) == str for el in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
