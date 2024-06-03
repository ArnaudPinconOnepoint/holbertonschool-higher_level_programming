#!/usr/bin/python3
"""
This module contains class BaseGeometry.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""
    def __init__(self, size):
        """
        Initialize the Square with size.
        Parameters:
        - size: The size of the square.
        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is not positive.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.
        Returns:
        - The area of the square (size * size).
        """
        return self.__size * self.__size
