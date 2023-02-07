#!/usr/bin/python3
"""Defining a module"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            A public method that retrieves a dictionary representation of a
            Student instance
        """
        return self.__dict__
