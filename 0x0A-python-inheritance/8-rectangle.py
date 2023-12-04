#!/usr/bin/python3
"""create class Rectangle of BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """repr rectangle"""
    def __init__(self, width, height):
        """inits width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height == height
