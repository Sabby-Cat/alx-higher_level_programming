#!/usr/bin/python3
"""writes to file"""


def write_file(filename="", text=""):
    """opens and writes to file"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
