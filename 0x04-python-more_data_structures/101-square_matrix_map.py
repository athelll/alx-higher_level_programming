def square_matrix_map(matrix=[]):
    new_matrix = []
    for row in matrix:
        multiplied = []
        for elements in row:
            multiplied.append(elements * elements)
        new_matrix.append(multiplied)
    return new_matrix
