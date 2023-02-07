#!/usr/bin/python3
"""Defining a method"""


import json


def from_json_string(my_str):
    """
        A function that returns an object (Python data structure) represented
        by a JSON string
    """
    return json.loads(my_str)