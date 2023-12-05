#!/usr/bin/python3
"""append to file"""


def append_write(filename="", text=""):
    """wrates and appends to file"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
