#!/usr/bin/python3
"""This module contains class Rectangle"""


class Rectangle:
    """This class is Rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter size"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter size"""
        try:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        except (TypeError, ValueError) as e:
            raise e
        
    @property
    def height(self):
        """Getter size"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter size"""
        try:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        except (TypeError, ValueError) as e:
            raise e
