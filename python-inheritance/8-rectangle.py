#!/usr/bin/python3
"""
This module contains class BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""
    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.
        Parameters:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        Raises:
        - TypeError: If width or height is not an integer.
        - ValueError: If width or height is not positive.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
