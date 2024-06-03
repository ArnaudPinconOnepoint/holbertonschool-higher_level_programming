#!/usr/bin/python3
"""
This module contains class BaseGeometry.
"""


class BaseGeometry:
    """Base class for geometric shapes."""
    def area(self):
        """
        Calculate the area of the geometric shape.
        Raises an Exception since it is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate that a parameter is a positive integer.
        
        Parameters:
        - name: The name of the parameter.
        - value: The value of the parameter.
        
        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
