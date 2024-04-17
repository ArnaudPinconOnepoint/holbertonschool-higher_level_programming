#!/usr/bin/python3
"""This module contains class Square"""


class Square:
    """This class is Square"""
    __size = 10

    def __init__(self, size=0):
        """Initial instance"""
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            self.__size = size
        except (TypeError, ValueError) as e:
            raise e
