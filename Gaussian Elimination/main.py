import numpy as np


def solve_system_of_equations(A, b):
    try:
        solution = np.linalg.solve(A, b)
        return solution
    except np.linalg.LinAlgError:
        return "System has no unique solution"


def gaussian_elimination(A, b):
    n = len(A)

    augmented = np.column_stack([A, b])
    augmented = augmented.astype(float)

    for i in range(n):
        pivot_row = i
        max_val = abs(augmented[i][i])

        for k in range(i + 1, n):
            if abs(augmented[k][i]) > max_val:
                max_val = abs(augmented[k][i])
                pivot_row = k

        if pivot_row != i:
            augmented[i], augmented[pivot_row] = augmented[pivot_row].copy(), augmented[i].copy()

        if abs(augmented[i][i]) < 1e-10:
            return "System has no unique solution"

        pivot = augmented[i][i]
        augmented[i] = augmented[i] / pivot

        for j in range(i + 1, n):
            factor = augmented[j][i]
            augmented[j] = augmented[j] - factor * augmented[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = augmented[i][-1]
        for j in range(i + 1, n):
            x[i] = x[i] - augmented[i][j] * x[j]
    return x


A = np.array([
    [3, -1, -1],
    [1, 1, 0],
    [2, 0, -3]
])

b = np.array([5, 0, 2])

print(solve_system_of_equations(A, b))
print(gaussian_elimination(A, b))
