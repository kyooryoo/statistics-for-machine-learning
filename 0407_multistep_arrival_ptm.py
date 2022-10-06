import numpy as np

A = np.array([[1,0,0,0],[.2,.4,.4,0],[0,.4,.4,.2],[0,0,0,1]])

def get_matrix_pow(matrix, n):
    ret = matrix
    for i in range(n):
        ret = np.dot(ret, A)
    print(F"{n} steps:\n{ret}\n")

get_matrix_pow(A,1)
get_matrix_pow(A,10)
get_matrix_pow(A,1000)
