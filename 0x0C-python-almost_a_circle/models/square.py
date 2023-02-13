#!/usr/bin/python3
"""Defining a square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class instantiation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            This method returns [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """A method to retrieve public instance of size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """A method that sets width and height"""
        self.width = value 
        self.height = value

    def update(self, *args, **kwargs):
        """
            A public method that assigns a key/value argument to attributes:
            **kwargs must be skipped if *args exists and is not empty
            1st argument should be the id attribute,
            2nd argument should be the width attribute,
            3rd argument should be the height attribute,
            4th argument should be the x attribute,
            5th argument should be the y attribute.
        """
        num_args = len(args)
        if num_args > 0:
            self.id = args[0]
        if num_args > 1:
            self.size = args[1]
        if num_args > 2:
            self.x = args[2]
        if num_args > 3:
            self.y = args[3]
        if num_args == 0:
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """
            This method returns the dictionary representation of a Square
        """
        my_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_dict
