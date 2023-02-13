#!/usr/bin/python3
"""Defining a module"""

import json


class Base:
    """Defining a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
            A class method that writes the JSON string representation of
            list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
            A static method that returns the list of the JSON string
            representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            A class method that returns an instance with all attributes
            already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 1)
            else:
                new_inst = cls(1)
            new_inst.update(**dictionary)
            return (new_inst)

    @classmethod
    def load_from_file(cls):
        """
            A class method that returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode="r") as f:
                dict_list = Base.from_json_string(f.read())
                return [cls.create(**x) for x in dict_list]
        except IOError:
            return []
