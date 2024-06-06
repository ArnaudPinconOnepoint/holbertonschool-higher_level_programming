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
        """Retrieves a filtered or full
        dictionary representation of a
        Student instance."""
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            filtered_attrs = []
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_attrs.append(attr)
            attrs = filtered_attrs
        json_dict = {}
        for attr in attrs:
            json_dict[attr] = getattr(self, attr)
        return json_dict
