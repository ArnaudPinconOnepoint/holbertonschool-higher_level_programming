#!/usr/bin/python3
"""This module contains class Square"""


class Square:
    """This class is Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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
    @property
    def position(self):
        """Getter position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter position"""
        try:
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            x, y = value
            if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
                raise ValueError("position coordinates must be positive integers")
            self.__position = value
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
            for j in range (0, self.__position[1]):
                print()
            print(' '*self.__position[0], end="")
            for i in range(1, self.area()+1):
                if (i % self.__size):
                    print("#", end="")
                else:
                    print("#", end="\n")
                    print(' '*self.__position[0], end="")
