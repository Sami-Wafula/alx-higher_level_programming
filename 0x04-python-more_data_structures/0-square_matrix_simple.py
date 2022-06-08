#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        for i in row:
            new.append(i*i)
    new_matrix = []
    while new != []:
        new_matrix.append(new[:3])
        new = new[3:]

    return new_matrix
