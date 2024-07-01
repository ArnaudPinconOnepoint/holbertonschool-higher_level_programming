#!/usr/bin/python3
"""
Module de tests pour la classe Base.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Classe de tests pour la classe Base.
    """

    def test_auto_increment_id(self):
        """
        Teste l'assignation automatique d'un ID
        supérieur de 1 à celui du précédent existant.
        """
        base_obj1 = Base()
        base_obj2 = Base()
        self.assertEqual(base_obj2.id, base_obj1.id + 1)

    def test_passed_id(self):
        """
        Teste la sauvegarde de l'ID passé en argument.
        """
        base_obj = Base(89)
        self.assertEqual(base_obj.id, 89)

    def test_to_json_string_none(self):
        """
        Teste la méthode to_json_string avec None comme argument.
        """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """
        Teste la méthode to_json_string avec une liste vide comme argument.
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list_with_dict(self):
        """
        Teste la méthode to_json_string avec une liste contenant un dictionnaire comme argument.
        """
        input_list = [{'id': 12}]
        expected_output = '[{"id": 12}]'
        self.assertEqual(Base.to_json_string(input_list), expected_output)

    def test_to_json_string_return_type(self):
        """
        Vérifie que la méthode to_json_string retourne une chaîne de caractères.
        """
        self.assertIsInstance(Base.to_json_string([]), str)

    def test_from_json_string_none(self):
        """
        Teste la méthode from_json_string avec None comme argument.
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        """
        Teste la méthode from_json_string avec une chaîne vide comme argument.
        """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid_string(self):
        """
        Teste la méthode from_json_string avec une chaîne JSON valide comme argument.
        """
        input_string = '[{ "id": 89 }]'
        expected_output = [{'id': 89}]
        self.assertEqual(Base.from_json_string(input_string), expected_output)

    def test_from_json_string_return_type(self):
        """
        Vérifie que la méthode from_json_string retourne une liste.
        """
        self.assertIsInstance(Base.from_json_string("[]"), list)


if __name__ == '__main__':
    unittest.main()
