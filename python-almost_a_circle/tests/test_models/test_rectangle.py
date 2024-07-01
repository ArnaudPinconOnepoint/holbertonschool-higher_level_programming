#!/usr/bin/python3
"""
Module de tests pour la classe Rectangle.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Classe de tests pour la classe Rectangle.
    """

    def test_constructor_exists(self):
        """
        Vérifie l'existence du constructeur de Rectangle avec différentes combinaisons d'arguments.
        """
        Rectangle(1, 2)
        Rectangle(1, 2, 3)
        Rectangle(1, 2, 3, 4)
        Rectangle("1", 2)
        Rectangle(1, "2")
        Rectangle(1, 2, "3")
        Rectangle(1, 2, 3, "4")
        Rectangle(1, 2, 3, 4, 5)
        Rectangle(-1, 2)
        Rectangle(1, -2)
        Rectangle(0, 2)
        Rectangle(1, 0)
        Rectangle(1, 2, -3)
        Rectangle(1, 2, 3, -4)

    def test_area_exists(self):
        """
        Vérifie l'existence de la méthode area().
        """
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_str_exists(self):
        """
        Vérifie l'existence de la méthode __str__() pour Rectangle.
        """
        rect = Rectangle(2, 3, 1, 1, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 1/1 - 2/3")

    def test_display_exists(self):
        """
        Vérifie l'existence de la méthode display() pour Rectangle.
        """
        rect = Rectangle(2, 3)
        self.assertIsNone(rect.display())

    def test_to_dictionary_exists(self):
        """
        Vérifie l'existence de la méthode to_dictionary() pour Rectangle.
        """
        rect = Rectangle(2, 3, 1, 1, 1)
        self.assertEqual(rect.to_dictionary(), {'id': 1, 'width': 2, 'height': 3, 'x': 1, 'y': 1})

    def test_update_exists(self):
        """
        Vérifie l'existence de la méthode update() pour Rectangle.
        """
        rect = Rectangle(2, 3, 1, 1, 1)
        rect.update(89)
        self.assertEqual(rect.id, 89)
        rect.update(89, 1)
        self.assertEqual(rect.width, 1)
        rect.update(89, 1, 2)
        self.assertEqual(rect.height, 2)
        rect.update(89, 1, 2, 3)
        self.assertEqual(rect.x, 3)
        rect.update(89, 1, 2, 3, 4)
        self.assertEqual(rect.y, 4)
        rect.update(id=89)
        self.assertEqual(rect.id, 89)
        rect.update(id=89, width=1)
        self.assertEqual(rect.width, 1)
        rect.update(id=89, width=1, height=2)
        self.assertEqual(rect.height, 2)
        rect.update(id=89, width=1, height=2, x=3)
        self.assertEqual(rect.x, 3)
        rect.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(rect.y, 4)

    def test_create_exists(self):
        """
        Vérifie l'existence de la méthode create() pour Rectangle.
        """
        rect = Rectangle.create(**{'id': 89})
        self.assertEqual(rect.id, 89)
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(rect.width, 1)
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.height, 2)
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.x, 3)
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.y, 4)

    def test_save_to_file_exists(self):
        """
        Vérifie l'existence de la méthode save_to_file() pour Rectangle.
        """
        Rectangle.save_to_file(None)
        Rectangle.save_to_file([])
        Rectangle.save_to_file([Rectangle(1, 2)])

    def test_load_from_file_exists(self):
        """
        Vérifie l'existence de la méthode load_from_file() pour Rectangle.
        """
        with self.assertRaises(FileNotFoundError):
            Rectangle.load_from_file()

    def test_load_from_file_when_file_exists(self):
        """
        Vérifie l'existence de la méthode load_from_file() pour Rectangle quand le fichier existe.
        """
        # Vous pouvez remplacer le chemin par celui de votre fichier de test existant
        pass


if __name__ == '__main__':
    unittest.main()
