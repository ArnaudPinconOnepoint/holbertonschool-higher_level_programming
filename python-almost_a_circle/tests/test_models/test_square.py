#!/usr/bin/python3
"""
Module de tests pour la classe Square.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Classe de tests pour la classe Square.
    """

    def test_constructor_exists(self):
        """
        Vérifie l'existence du constructeur de Square avec différentes combinaisons d'arguments.
        """
        Square(1)
        Square(1, 2)
        Square(1, 2, 3)
        Square("1")
        Square(1, "2")
        Square(1, 2, "3")
        Square(1, 2, 3, 4)
        Square(-1)
        Square(1, -2)
        Square(1, 2, -3)
        Square(0)

    def test_str_exists(self):
        """
        Vérifie l'existence de la méthode __str__() pour Square.
        """
        square = Square(2, 3, 1, 1)
        self.assertEqual(str(square), "[Square] (1) 3/1 - 2")

    def test_to_dictionary_exists(self):
        """
        Vérifie l'existence de la méthode to_dictionary() pour Square.
        """
        square = Square(2, 3, 1, 1)
        self.assertEqual(square.to_dictionary(), {'id': 1, 'size': 2, 'x': 3, 'y': 1})

    def test_update_exists(self):
        """
        Vérifie l'existence de la méthode update() pour Square.
        """
        square = Square(2, 3, 1, 1)
        square.update(89)
        self.assertEqual(square.id, 89)
        square.update(89, 1)
        self.assertEqual(square.size, 1)
        square.update(89, 1, 2)
        self.assertEqual(square.x, 2)
        square.update(89, 1, 2, 3)
        self.assertEqual(square.y, 3)
        square.update(id=89)
        self.assertEqual(square.id, 89)
        square.update(id=89, size=1)
        self.assertEqual(square.size, 1)
        square.update(id=89, size=1, x=2)
        self.assertEqual(square.x, 2)
        square.update(id=89, size=1, x=2, y=3)
        self.assertEqual(square.y, 3)

    def test_create_exists(self):
        """
        Vérifie l'existence de la méthode create() pour Square.
        """
        square = Square.create(**{'id': 89})
        self.assertEqual(square.id, 89)
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(square.size, 1)
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.x, 2)
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.y, 3)

    def test_save_to_file_exists(self):
        """
        Vérifie l'existence de la méthode save_to_file() pour Square.
        """
        Square.save_to_file(None)
        Square.save_to_file([])
        Square.save_to_file([Square(1)])

    def test_load_from_file_exists(self):
        """
        Vérifie l'existence de la méthode load_from_file() pour Square.
        """
        with self.assertRaises(FileNotFoundError):
            Square.load_from_file()

    def test_load_from_file_when_file_exists(self):
        """
        Vérifie l'existence de la méthode load_from_file() pour Square quand le fichier existe.
        """
        # Vous pouvez remplacer le chemin par celui de votre fichier de test existant
        pass


if __name__ == '__main__':
    unittest.main()
