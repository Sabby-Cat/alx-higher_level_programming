#!/usr/bin/python3
"""defines rectangle class"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """creates rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width get/set"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """height get/set"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
