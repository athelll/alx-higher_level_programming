#!/usr/bin/python3
"""

pascal_triangle


"""


def pascal_triangle(n):
    """
    pascal_triangle function
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    result = [[1]]
    for i in range(n - 1):
        result.append([a+b for a, b
                       in zip([0] + result[-1], result[-1] + [0])])
    return result
