#!/usr/bin/python3
"""defines square class"""


class Square:
    """repesents a square"""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): size of new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return current area of square."""
        return self.__size ** 2
