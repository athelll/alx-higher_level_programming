#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        highest, person = 0, ''
        for key, value in a_dictionary.items():
            if value > highest:
                highest, person = value, key
        return person
    else:
        return None
