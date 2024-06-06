#!/usr/bin/python3
"""
This module contains something
"""

import json


def load_from_json_file(filename):
    """ description """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
