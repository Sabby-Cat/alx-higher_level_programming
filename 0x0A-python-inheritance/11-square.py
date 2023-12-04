#!/usr/bin/python3
"""square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """repr a square"""
    def __init__(self, size):
        """init a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"return area of square"""
        return self.__size ** 2

    def __str__(self):
        """string representation"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
