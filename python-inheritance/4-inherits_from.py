#!/usr/bin/python3
"""
This module's is documented
"""


def inherits_from(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class; False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
