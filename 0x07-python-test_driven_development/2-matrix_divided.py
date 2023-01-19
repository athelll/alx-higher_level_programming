#!/usr/bin/python3
"""
Module: 2-matrix_divided
------------------------
Function: matrix_divided
------------------------
Args: 1) Matrix <list>
      2) div <int/float>
------------------------
Func. Returns: a new matrix
with its elements divided by div
"""


def matrix_divided(matrix, div):
    """
    This is the function that
    divides the elements of a matrix
    with div
    """
    new = []
    num_type = (int, float)
    fixed_len = len(matrix[0])

    if type(div) not in num_type:
        raise TypeError('div must be a number')
        return
    elif div == 0:
        raise ZeroDivisionError('division by zero')
        return

    for row in matrix:
        if len(row) != fixed_len:
            raise TypeError('Each row of the matrix must have the same size')
            return

        try:
            new.append(list(map(lambda a: round(a/div, 2), row)))
        except (TypeError, ValueError):
            raise TypeError('matrix must be a matrix (list of lists)\
                  of integers/floats')
            return
    return new
