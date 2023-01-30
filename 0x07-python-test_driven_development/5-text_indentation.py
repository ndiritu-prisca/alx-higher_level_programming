#!/usr/bin/python3
"""
    A text indentation module.
    It has one function that indents texts wherever there is '.', '?' or ':'
    The function does not return rather it prints to stdout
"""


def text_indentation(text):
    """
        A function that indents a string passed as text and raises any error.
    """
    print("{}".format(len(text)))
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print("{}".format(char), end="")
            print()
            print()
        else:
            print("{}".format(char), end="")
