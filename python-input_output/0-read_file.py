#!/usr/bin/python3
"""
This module contains class BaseGeometry.
"""


def read_file(filename=""):
    """ Read File """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
