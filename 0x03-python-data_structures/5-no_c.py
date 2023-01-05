#!/usr/bin/python3
def no_c(my_string):
    s = "".join(c for c in my_string if c not in "cC")
    return s
