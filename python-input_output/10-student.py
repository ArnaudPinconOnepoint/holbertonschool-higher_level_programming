#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then saves them to a file.
"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a filtered or full dictionary representation of a Student instance."""
        if attrs is None:
            # Si attrs est None, retourne tous les attributs
            return self.__dict__
        # Sinon, filtre les attributs en fonction de attrs
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
