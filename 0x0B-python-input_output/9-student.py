#!/usr/bin/python3
"""student class"""


class Student:
    """repr a student"""
    def __init__(self, first_name, last_name, age):
        """initialises new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets json version of student"""
        return self.__dict__
