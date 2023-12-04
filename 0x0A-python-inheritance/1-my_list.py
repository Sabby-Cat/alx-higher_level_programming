#!/usr/bin/python3
"""mylist class"""


class MyList(list):
    """list subclass"""
    def __init__(slef):
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
