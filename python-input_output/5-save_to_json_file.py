#!/usr/bin/python3
"""
This module contains something
"""

import json


def save_to_json_file(my_obj, filename):
    """ description """
    representation = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(representation)
