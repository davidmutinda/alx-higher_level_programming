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
        if attrs is not None and all(isinstance(k, str) for k in attrs):
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.__dict__ = json
