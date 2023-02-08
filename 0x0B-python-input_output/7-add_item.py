#!/usr/bin/python3
"""

Contains function that adds and saves
to Python obj to JSON file; loads objects

"""

from sys import argv

save_json = __import__('5-save_to_json_file.py').save_to_json_file
laod_json = __import__('6-load_from_json_file.py').load_from_json_file

filename = 'add_item.json'

try:
    existing = laod_json(filename)
except FileNotFoundError:
    existing = []

save_json(existing + argv[1:], filename)    
