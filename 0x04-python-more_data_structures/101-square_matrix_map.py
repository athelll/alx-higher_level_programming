def square_matrix_map(matrix=[]):
    new_matrix = []
    for row in matrix:
        multiplied = list(map(lambda a: a*a, row))
        new_matrix.append(multiplied)
    return new_matrix
