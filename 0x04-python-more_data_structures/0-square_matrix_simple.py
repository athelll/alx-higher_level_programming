#!/usr/bin/python3
# def square_matrix_simple(matrix=[]):
#    new_matrix = []
#    elements = []
#    for x in matrix:
#         elements = []
#         for y in x:
#             elements.append(y**2)
#         new_matrix.append(elements)
#    return new_matrix


def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = []
        for i, z in enumerate(matrix):
            new_matrix.append(list(map(lambda y: y**2, matrix[i])))
        return new_matrix
    return None
