#!/usr/bin/python3
"""
This module contains class BaseGeometry.
"""


def write_file(filename="", text=""):
    """ Write File """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    read_file(filename)

def read_file(filename=""):
    """ Read File """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(f"{read_data}", end='')