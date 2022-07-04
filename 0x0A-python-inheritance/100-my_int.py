#!/usr/bin/python3
"""
This module inherits from int
"""


class MyInt(int):
    """
    This class inherits from int and has == and != operators inverted
    """
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
