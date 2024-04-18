#!/usr/bin/python3
"""This module contains class Square"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.size ** 2

    def my_print(self):
        """Print the square with the given position"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            print(' ' * self.position[0], end="")
            for i in range(1, self.area() + 1):
                print("#", end="")
                if i % self.size == 0:
                    print()
                    if i != self.area():
                        print(' ' * self.position[0], end="")
