#!/usr/bin/python3
"""
This module contains class Base.
"""

import json


class Base:
    """
    Base class for creating objects with unique identifiers.
    """

    __nb_objects = 0  # private class attribute for counting instances

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int, optional): Identifier for the object. If not provided,
            it auto-increments using __nb_objects.
        """
        if id is not None:
            self.id = id  # assign id if provided
        else:
            Base.__nb_objects += 1  # increment class attribute
            self.id = Base.__nb_objects  # assign new value to id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation of
        list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries to be
            converted to JSON string.

        Returns:
            str: JSON string representation of list_dictionaries
            or "[]" if the list is empty or None.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string
        representation of list_objs to a file.

        Args:
            list_objs (list): List of instances inheriting from Base
            (e.g., list of Rectangle or Square instances).
        """
        filename = f"{cls.__name__}.json"  # Create filename
        if list_objs is None:
            list_objs = []

        # Convert list of objects to list of dictionaries
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        # Convert list of dictionaries to JSON string
        json_string = cls.to_json_string(list_dictionaries)

        # Write JSON string to file
        with open(filename, 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list represented by the JSON string.

        Args:
            json_string (str): String representing a list of dictionaries.

        Returns:
            list: List of dictionaries represented by json_string,
            or an empty list if json_string is None or empty.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)