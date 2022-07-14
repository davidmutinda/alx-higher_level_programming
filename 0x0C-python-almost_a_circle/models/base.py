#!/usr/bin/python3
"""
This module contains class Base
"""
import json


class Base:
    """
    The base of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON representation"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves JSON representation to file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            list_new = list()
            if list_objs:
                for inst in list_objs:
                    list_new.append(inst.to_dictionary())

            list_t = cls.to_json_string(list_new)
            f.write(list_t)
