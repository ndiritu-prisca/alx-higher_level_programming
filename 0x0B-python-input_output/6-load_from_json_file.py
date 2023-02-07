#!/usr/bin/python3
"""Defining a method"""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”"""
    with open(filename, mode='r') as f:
        return json.load(f)
