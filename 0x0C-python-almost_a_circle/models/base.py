#!/usr/bin/python3
"""module documentation"""
import json
import os


class Base:
    """class documentation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """function documentation"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function documentation"""
        if list_dictionaries is None or list_dictionaries == {}:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function documentation"""
        filename = '{}.json'.format(cls.__name__)
        my_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """function documentation"""
        if json_string is None or type(json_string) is not str:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function documentation"""

    @classmethod
    def create(cls, **dictionary):
        """function documentation"""
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """function documentation"""
        inst_list = []
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                dct_list = cls.from_json_string(file.read())
                for item in dct_list:
                    dummy = cls.create(**item)
                    inst_list.append(dummy)
                return inst_list
