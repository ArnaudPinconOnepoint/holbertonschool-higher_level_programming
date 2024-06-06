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
        """Retrieves a filtered or full dictionary representation of a Student instance."""
        if attrs is None:
            # Utilise tous les attributs si attrs est None
            attrs = self.__dict__.keys()
        else:
            # Filtrer les attributs en fonction de la liste attrs
            attrs = [attr for attr in attrs if hasattr(self, attr)]
        # Créer le dictionnaire JSON en utilisant les attributs filtrés ou tous les attributs
        json_dict = {}
        for attr in attrs:
            json_dict[attr] = getattr(self, attr)
        return json_dict
