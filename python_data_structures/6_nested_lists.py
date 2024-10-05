#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i]) - 1):
            print(mat[i][j], end = ' ')
        print(mat[i][len(mat[i]) - 1])

print_matrix(matrix)

