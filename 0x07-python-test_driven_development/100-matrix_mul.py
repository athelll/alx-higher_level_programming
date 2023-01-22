#!/usr/bin/python3
"""

Module: 100-matrix_mul
Function that can muliply 2 matrices

"""


def matrix_mul(m_a, m_b):

    """

    Func: matrix_mul
    Args: m_a, m_b list[list[int]]

    This functiom multiplies
    2 matrices

    """

    multi = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # checks is m_a or m_b is a list
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("{} must be a list".format(
            'm_a' if isinstance(m_b, list) else 'm_b'))

    # checks is m_a or m_b is a list of lists
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError('m_a must be a list of lists')
    elif not all(isinstance(i, list) for i in m_b):
        raise TypeError('m_b must be a list of lists')

    # check if list is empty or not
    if m_a == [] or m_b == []:
        raise TypeError("{} can't be empty".format(
            'm_a' if m_b == [] else 'm_b'))

    # check if row is equal to coloumn
    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")

    # check something
    len_check, len_check2 = len(m_a[0]), len(m_b[0])
    if not all(len_check == len(i) for i in m_a):
        raise TypeError('each row of m_a must be of the same size')
    elif not all(len_check2 == len(i) for i in m_b):
        raise TypeError('each row of m_b must be of the same size')

    # row of first matrix
    for i in range(len(m_a)):
        # coloumn of second matrix
        for j in range(len(m_b[0])):
            # row of second matrix
            for k in range(len(m_b)):
                multi[i][j] += m_a[i][k] * m_b[k][j]

    return multi
