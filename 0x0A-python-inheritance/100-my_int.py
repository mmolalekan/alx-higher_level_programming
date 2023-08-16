#!/usr/bin/python3
"""defines a class that imports from int"""


class MyInt(int):
    def __eq__(self, value):
        """overwrites != with =="""
        return self.real != value

    def __ne__(self, value):
        """overwrites == with !="""
        return self.real == value
