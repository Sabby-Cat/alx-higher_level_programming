#!/usr/bin/python3
"""
file for function
to add 2 nrs together
raising errors if not possible
"""

def add_integer(a, b=98):
    """
    adds 2 ints together 
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
