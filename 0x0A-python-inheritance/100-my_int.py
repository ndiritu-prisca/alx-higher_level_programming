#!/usr/bin/python3
"""Defining a module that inherits from int"""


class MyInt(int):
    """
        This class inherits from int although == and != operators are
        inverted
    """
    def __eq__(self, other):
        """Defines != comparison"""
        return (self.real != other)

    def __ne__(self, other):
        """Defines == comparison"""
        return (self.real == other)
