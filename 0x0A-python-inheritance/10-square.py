#!/usr/bin/python3
"""
This module inherits from class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
