#!/usr/bin/python3
"""defines square class"""


class Square:
    """repesents a square"""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set current size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return current area of square."""
        return self.__size ** 2
