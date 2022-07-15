#!/usr/bin/python3
"""
This module contains class Base
"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string"""
        if not json_string:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes set"""
        if cls.__name__ == "Square":
            r = cls(10)
        elif cls.__name__ == "Rectangle":
            r = cls(10, 10)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        filename = cls.__name__ + ".json"
        ret = list()
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                hld = f.read()
                news = cls.from_json_string(hld)
                for new in news:
                    ret.append(cls.create(**new))
            return ret
        except Exception:
            return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a json to csv"""
        filename = str(cls.__name__) + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for o in list_objs:
                    writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """return a list of class instances from.a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
