#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_be_popped = []
    for key, val in a_dictionary.items():
        if val == value:
            to_be_popped.append(key)
    for key in to_be_popped:
        a_dictionary.pop(key)
    return a_dictionary
