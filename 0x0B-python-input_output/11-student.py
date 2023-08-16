#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """A class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """instantiation with the following arguments"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """etrieves a dictionary representation of a Student instance"""
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            my_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    my_dict[attr] = getattr(self, attr)
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
