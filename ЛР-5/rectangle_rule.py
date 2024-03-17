import numpy as np


def rectangle_rule(matrix):
    for i in range(len(matrix)):
        matrix[i] = [elem / matrix[i][i] for elem in matrix[i]]
        for j in range(i + 1, len(matrix)):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, len(matrix) + 1):
                matrix[j][k] -= factor * extended_matrix[i][k]

        print(f"\nМатрица после {i+1}-го шага:")
        for row in matrix:
            print(row)

    solutions = np.zeros(len(matrix))
    for i in range(len(matrix) - 1, -1, -1):
        solutions[i] = (matrix[i][-1] - np.dot(matrix[i][:-1], solutions)) / extended_matrix[i][i]

    return solutions


extended_matrix = [[2, 1, 4, 16],
                   [3, 2, 1, 10],
                   [1, 3, 3, 16]]


result = rectangle_rule(extended_matrix)

print("\nРешения")

for x_index in range(len(result)):
    print(f"x{x_index+1} = {result[x_index]}")