#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)

    def __str__(self):
        """Sets the print behavior of the Square object."""
        ret = ""
        if self.__size > 0:
            for i in range(self.__position[1]):
                ret += '\n'
            for j in range(self.__size):
                ret += ' ' * self.__position[0]
                ret += '#' * self.__size + '\n'
        return ret[:-1]
