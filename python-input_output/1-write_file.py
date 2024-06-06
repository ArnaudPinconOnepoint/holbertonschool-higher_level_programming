#!/usr/bin/python3
"""
This module contains class BaseGeometry.
"""


def write_file(filename="", text=""):
    """ Write File """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
