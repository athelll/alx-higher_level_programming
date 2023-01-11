#!/usr/bin/python3
def my_reduce(func, lists=()):
    return func(lists[0], lists[1])


def weight_average(my_list=[]):
    numerator = 0
    denominator = 0
    for i, j in enumerate(my_list):
        numerator += my_reduce(lambda a, b: a * b, my_list[i])
        denominator += my_list[i][-1]
    return numerator/denominator
