#!/usr/bin/python3
"""defines rectangle class"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """deletes instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        """returns new rec that is square"""
        return cls(size, size)

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
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns rectangle with biggest area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """returns readable string"""
        ret = ""
        for i in range(self.__height):
            ret += str(self.print_symbol) * self.__width + "\n"
        return ret

    def __repr__(self):
        """return str repr of rec for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
