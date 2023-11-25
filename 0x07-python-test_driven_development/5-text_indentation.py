#!/usr/bin/python3
"""defines function tesxt indent"""


def text_indentation(text):
    """prints out test file"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    for l in text:
        if c == 0:
            if l == ' ':
                continue
            else:
                c = 1
        if c == 1:
            if l == ':' or l == '.' or l == '?':
                print(l)
                print()
                c = 0
            else:
                print(l, end="")