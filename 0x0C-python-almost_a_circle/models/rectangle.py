#!/usr/bin/python3
"""
This module contains Rectangle class that
inherits from Base
"""
from .base import Base


class Rectangle(Base):
    """
    This class defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check_for_error(self, name, value, status=False):
        """
        Checks if there is an error
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        elif not status:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

        elif value < 1:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.check_for_error("width", value, True)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.check_for_error("height", value, True)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.check_for_error("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.check_for_error("y", value)
        self.__y = value
