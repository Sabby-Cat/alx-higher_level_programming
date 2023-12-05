#!/usr/bin/python3
"""def read file"""


def read_file(filename=""):
    """function to read file"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
