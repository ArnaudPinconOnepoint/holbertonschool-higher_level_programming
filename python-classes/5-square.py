#!/usr/bin/python3
"""This module contains class Square"""


class Square:
    """This class is Square"""
    __size = 10

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size"""
        try:
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except (TypeError, ValueError) as e:
            raise e

    def area(self):
        """Return area"""
        area = self.__size*self.__size
        return area

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(1, self.area()+1):
                if (i % self.__size):
                    print("#", end="")
                else:
                    print("#", end="\n")
