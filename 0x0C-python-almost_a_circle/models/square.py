#!/usr/bin/python3
"""defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def size(self):
        """module Square size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """module Square size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'size': self.size,
            'width': self.width
        }
