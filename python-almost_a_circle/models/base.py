#!/usr/bin/python3
"""
This module contains class Base.
"""

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
