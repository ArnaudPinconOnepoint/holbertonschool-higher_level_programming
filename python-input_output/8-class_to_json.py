#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then saves them to a file.
"""


def class_to_json(obj):
    """Returns a dictionary description for JSON serialization of an object."""
    if not hasattr(obj, '__dict__'):
        return {}  # If object has no attribute, render empty
    result = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            result[attr_name] = attr_value
    return result
