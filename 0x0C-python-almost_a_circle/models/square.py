#!/usr/bin/python3
"""module documentation"""
import importlib
Rectangle = importlib.import_module('models.rectangle').Rectangle


class Square(Rectangle):
    """calss documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        """function documentation"""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """"function documentation"""
        return self.width

    @size.setter
    def size(self, value):
        """function documentation"""
        self.width = value
        self.height = value

    def __str__(self):
        """function documentation"""
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """function documentation"""
        if len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for arg, attr in zip(args, attrs):
                setattr(self, attr, arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """function documentation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
