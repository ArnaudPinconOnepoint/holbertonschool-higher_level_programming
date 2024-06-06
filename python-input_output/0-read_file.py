#!/usr/bin/python3
"""
This module contains something
"""


def read_file(filename=""):
    """ Read File """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(f"{read_data}", end='')
