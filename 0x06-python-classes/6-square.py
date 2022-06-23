#!/usr/bin/python3
"""This module defines a square class
"""


class Square:
    """Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
        self.__size = size

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

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print('')
            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
