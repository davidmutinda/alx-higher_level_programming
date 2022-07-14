#!/usr/bin/python3
"""
This module contains Square class which inherits
from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    This class defines a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The str method"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.__height

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif args:
            i = 0
            for arg in args:
                if not i:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
