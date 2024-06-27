#!/usr/bin/python3
"""
This module contains the Rectangle class that inherits from Base.
"""

Base = __import__('base').Base

class Rectangle(Base):
    """
    A class representing a Rectangle, inheriting from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle's position.
        y (int): y-coordinate of the rectangle's position.
        id (int): Identifier for the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position (default is 0).
            y (int, optional): y-coordinate of the rectangle's position (default is 0).
            id (int, optional): Identifier for the rectangle (default is None, auto-assigned by Base).
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # Call super class constructor with id

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle instance by printing it with '#' characters,
        considering the x and y coordinates.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Override the string representation of Rectangle.

        Returns:
            str: Formatted string representing the rectangle instance.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle using positional and keyword arguments.
        Positional arguments take precedence over keyword arguments if both are provided.

        Args:
            *args (int): Arguments to update the attributes in the specified order.
                1st argument: id
                2nd argument: width
                3rd argument: height
                4th argument: x
                5th argument: y
            **kwargs (dict): Key-value pairs to update the attributes.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

# Example usage:
if __name__ == "__main__":
    rect = Rectangle(5, 3)  # Creates a rectangle with width 5, height 3 (default x=0, y=0)
    print(rect)  # Output: [Rectangle] (<id>) <x>/<y> - <width>/<height>

    rect.update(5, 9, 6, 2, 3)  # Updates id to 5, width to 9, height to 6, x to 2, y to 3
    print(rect)  # Output: [Rectangle] (5) 2/3 - 9/6

    rect.update(id=10, width=15, height=20, x=5, y=5)  # Updates attributes using keyword arguments
    print(rect)  # Output: [Rectangle] (10) 5/5 - 15/20
