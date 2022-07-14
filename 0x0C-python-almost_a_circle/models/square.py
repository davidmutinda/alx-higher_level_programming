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
