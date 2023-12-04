#/usr/bin/python3
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

    def area(self):
        """Return area of Rect"""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str() repr of Rect"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
