#!/usr/bin/python3
"""This module contains class BaseGeometry"""

class BaseGeometry:
    """
    Base class for geometric shapes.
    """
    
    
    def area(self):
        """
        Calculate the area of the geometric shape.
        Raises an Exception since it is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
