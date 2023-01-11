#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str) | (roman_string is None):
        return 0
    if roman_string == '':
        return 0
    sums = 0
    ints = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for a, b in zip(roman_string, roman_string[1:]):
        if a not in ints:
            return 0
        elif ints[a] >= ints[b]:
            sums += ints[a]
        else:
            sums -= ints[a]
    sums += ints[roman_string[-1]]
    return sums
