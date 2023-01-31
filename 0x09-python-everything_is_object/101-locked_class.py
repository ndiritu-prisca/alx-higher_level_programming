#!/usr/bin/python3
"""Defining a class that prevents the user from dynamically creating new
instance attributes, except if the new instance attribute is called first_name
"""


class LockedClass:
    """A class with no object or class attribute"""
    __slots__ = ["first_name"]
