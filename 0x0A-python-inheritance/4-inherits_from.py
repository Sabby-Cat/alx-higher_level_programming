#!/usr/bin/python3
"""checks if inherits"""


def inherits_from(obj, a_class):
    """class checking if inherits"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
