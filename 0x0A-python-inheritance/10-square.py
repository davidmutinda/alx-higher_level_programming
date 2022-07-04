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
        super().__init__(size, size)
