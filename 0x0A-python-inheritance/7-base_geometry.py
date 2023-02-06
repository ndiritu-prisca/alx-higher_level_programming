#!/usr/bin/python3
"""Defining an a class"""


class BaseGeometry:
    """This class has one public instance method"""
    def area(self):
        """
            This function raisesan Exception with the message area() is not
            implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            A method that validates value.
            Name is assumed to always be a string
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
