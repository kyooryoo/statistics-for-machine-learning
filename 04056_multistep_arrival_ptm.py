import numpy as np

A = np.array([[.7,.2,.1],[.3,.5,.2],[.2,.4,.4]])

def get_matrix_pow(matrix, n):
    ret = matrix
    for i in range(n):
        ret = np.dot(ret, A)
    print(F"{n} steps:\n{ret}\n")

# 注意多次迭代后每行结果都是一样，即当前状态无关
get_matrix_pow(A,1)
get_matrix_pow(A,3)
get_matrix_pow(A,10)
get_matrix_pow(A,100)
get_matrix_pow(A,1000)
