#!/usr/bin/python3
""" rotate 2d matrix program """


def rotate_2d_matrix(matrix):
    """ return the rotated matrix """
    matrix.reverse()
    mat = [[row[i] for row in matrix] for i in range(len(matrix))]
    j = 0
    for row in matrix:
        for i in range(len(row)):
            row[i] = mat[j][i]
        j += 1
