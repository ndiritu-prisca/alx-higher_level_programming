#!/usr/bin/python3
"""MagicClass that works as a given python bytecode"""


import math


class MagicClass:
    """Defining a MagicClass"""
    def __init__(self, radius=0):
        """Initializing an instance of a circle that is a MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """A method that returns area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """A method that returns circumference of a circle"""
        return 2 * math.pi * self.__radius
