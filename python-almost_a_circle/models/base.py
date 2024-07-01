#!/usr/bin/python3
"""
This module contains the Base class.
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
        Class method that writes the JSON string representation
        of list_objs to a file.

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

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes already set
        using the dictionary provided.

        Args:
            **dictionary (dict): Dictionary
            containing attribute names and values.

        Returns:
            instance: Instance of the class with
            attributes set from dictionary.
        """
        if 'size' in dictionary:
            dummy_instance = cls(1)
        else:
            dummy_instance = cls(1, 1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances loaded from a JSON file.

        Returns:
            list: List of instances loaded from the JSON file.
                If the file doesn't exist, returns an empty list.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as f:
                json_string = f.read()  # Read JSON string from file
        except FileNotFoundError:
            return []  # Return empty list if file doesn't exist

        # Convert JSON string to list of dictionaries
        list_dicts = cls.from_json_string(json_string)
        # Create instances from dictionaries
        instances = [cls.create(**dict_obj) for dict_obj in list_dicts]
        return instances
