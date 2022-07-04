#!/usr/bin/python3
"""
This module contains class BaseGeometry
"""


class BaseGeometry:
    """
    This class raises an exception when area() is called
    """
    def area(self):
        raise Exception("area() is not implemented")
