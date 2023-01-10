#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        if key == keys:
            a_dictionary.pop(key)
            break
    return a_dictionary
