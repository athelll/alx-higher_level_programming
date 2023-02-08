#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    parsed_json = json.dumps(my_obj)
    
    with open(filename, mode="w") as f:
        f.write(parsed_json)
