#!/usr/bin/python3
# from functools import reduce
# def uniq_add(my_list=[]):
#     list_set = set(my_list)
#     sums = reduce(lambda x,y : x+y, list_set)
#     return sums


# Requested Version
def uniq_add(my_list=[]):
    if my_list is not None:
        sums = 0
        list_set = set(my_list)
        for i in list_set:
            sums += i
        return sums
    return None
