#!/usr/bin/python3
"""defines function text indent"""


def text_indentation(text):
    """prints out test file"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    for le in text:
        if c == 0:
            if le == ' ':
                continue
            else:
                c = 1
        if c == 1:
            if le == ':' or le == '.' or le == '?':
                print(le)
                print()
                c = 0
            else:
                print(le, end="")
