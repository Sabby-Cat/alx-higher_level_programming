#!/usr/bin/python3
"""func that adds attri to object"""


def add_attribute(obj, att, value):
    """Add new attribute to object or raise error"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
