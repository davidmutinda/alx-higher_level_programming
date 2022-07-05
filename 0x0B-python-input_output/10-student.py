#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    This class defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            for key, value in self.__dict__.items():
                if key == i:
                    new_dict[key] = value
        return new_dict
