#!/usr/bin/python3
"""Defining a square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class instantiation"""
        Rectangle.__init__(self, width=size, height=size, x, y, id)
