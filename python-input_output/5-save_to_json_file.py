#!/usr/bin/python3
"""
This module contains something
"""

import json


def save_to_json_file(my_obj, filename):
    """ description """
    try:
        # Convert the object to a JSON string
        representation = json.dumps(my_obj, default=list)
        
        # Write the JSON string to a file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(representation)
    
    except PermissionError as e:
        print(f"[PermissionError] {e}")
