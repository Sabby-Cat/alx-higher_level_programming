#!/usr/bin/python3
"""defines square class"""


class Square:
    """repesents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): size of new square.
            position (int, int): position of new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set current position of square."""
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
        """Return current area of square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
