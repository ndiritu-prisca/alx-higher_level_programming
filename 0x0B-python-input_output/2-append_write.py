#!/usr/bin/python3
"""Defining a method that appends text"""


def append_write(filename="", text=""):
    """
        A function that appends a string at the end of a text file (UTF8) and
        returns the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
