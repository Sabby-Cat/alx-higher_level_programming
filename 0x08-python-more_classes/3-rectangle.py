#!/usr/bin/python3
"""defines rectangle class"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """init rectangle"""
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
        self.__width = value

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
        self.__height = value

    def area(self):
        """gets area of rec"""
        return self.__width * self.__height

    def perimeter(self):
        """gets perimeter of rec"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        """returns readable string"""
        ret = ""
        if self.__height == 0 or self.__width == 0:
            return ret
        for i in range(self.__height - 1):
            ret += "#" * self.__width + "\n"
        return ret + "#" * self.__width
