import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    matrix = np.array(A)
    r, c = matrix.shape

    t_matr = np.zeros((c, r), dtype=matrix.dtype)

    for i in range(r):
        for j in range(c):
            t_matr[j][i] = matrix[i][j]

    return t_matr