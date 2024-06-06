#!/usr/bin/python3
"""
This module contains class BaseGeometry.
"""


def append_write(filename="", text=""):
    """ Write File """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        size = len(content)
    return size
