#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then saves them to a file.
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict repr of a Stud inst."""
        if attrs is None:
            # If attrs is None, retrieve all attributes
            return self.__dict__
        # Filter the attributes based on attrs list
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

    def reload_from_json(self, json_data):
        """Repl all attr with val from a JSON dict"""
        for attr, value in json_data.items():
            setattr(self, attr, value)
