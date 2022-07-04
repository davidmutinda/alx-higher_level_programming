#!/usr/bin/python3
"""
This module contains class BaseGeometry
"""


class BaseGeometry:
    """
    The area() method raises an exception when called
    """
    def area(self):
        raise Exception("area() is not implemented")

    """
    The method below validates value
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
