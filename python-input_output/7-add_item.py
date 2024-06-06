#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then saves them to a file.
"""

import sys
import importlib

save_module = importlib.import_module('5-save_to_json_file')
save_to_json_file = save_module.save_to_json_file
load_module = importlib.import_module('6-load_from_json_file')
load_from_json_file = load_module.load_from_json_file

filename = "add_item.json"

try:
    # Load the existing list from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list
    items = []

# Add all arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
