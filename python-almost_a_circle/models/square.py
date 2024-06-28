#!/usr/bin/python3
"""
This module contains the Square class that inherits from Rectangle.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a Square, inheriting from Rectangle.
    Attributes:
        size (int): Size of the square (both width and height).
        x (int): x-coordinate of the square's position.
        y (int): y-coordinate of the square's position.
        id (int): Identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Args:
            size (int): Size of the square (both width and height).
            x (int, optional): x-coordinate of the square's
            position (default is 0).
            y (int, optional): y-coordinate of the square's
            position (default is 0).
            id (int, optional): Identifier for the square
            (default is None, auto-assigned by Base).
        """
        super().__init__(size, size, x, y, id)
        # Call the super class with width and height equal to size

    def __str__(self):
        """
        Override the string representation of Square.

        Returns:
            str: Formatted string representing the square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter for size attribute.
        Returns:
            int: Size of the square (both width and height).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.
        Args:
            value (int): Size of the square (both width and height).
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square.
        Args:
            *args: List of non-keyworded arguments in the order:
                1. id
                2. size
                3. x
                4. y
            **kwargs: Dictionary of key/value arguments.
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation
        of the square.
        Returns:
            dict: Dictionary containing id,
            size, x, and y attributes.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
