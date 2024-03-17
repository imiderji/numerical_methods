import numpy as np


def single_division_method(matrix):
    for i in range(len(matrix)):
        max_index = max(range(i, len(matrix)), key=lambda x: abs(matrix[x][i]))

        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]

        matrix[i] = [elem / matrix[i][i] for elem in matrix[i]]

        for j in range(i + 1, len(matrix)):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(len(matrix[i]))]

        print(f"\nМатрица после {i}-го шага:")
        for row in matrix:
            print(row)

    solutions = np.zeros(len(matrix))
    for i in range(len(matrix) - 1, -1, -1):
        solutions[i] = ((matrix[i][-1] - np.dot(matrix[i][:-1], solutions)) / matrix[i][i])

    return solutions


extended_matrix = [[5, 0, 1, 11],
                   [2, 6, -2, 8],
                   [-3, 2, 10, 6]]

result = single_division_method(extended_matrix)

print("\nРешения")

for x_index in range(len(result)):
    print(f"x{x_index+1} = {result[x_index]}")
