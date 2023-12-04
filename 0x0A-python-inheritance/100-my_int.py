#!/usr/bin/python3
"""Defines myint class"""


class MyInt(int):
    """repr myint class"""

    def __eq__(self, value):
        """makes == !="""
        return self.real != value

    def __ne__(self, value):
        """makes != =="""
        return self.real == value
