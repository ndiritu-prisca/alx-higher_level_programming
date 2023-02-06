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
