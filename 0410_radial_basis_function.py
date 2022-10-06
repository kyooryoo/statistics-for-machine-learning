from random import gauss
import numpy as np

def gaussian_kernel(x1, x2, l=1.0, sigma_f=1.0):
    m, n = x1.shape[0], x2.shape[0]
    dist_matrix = np.zeros((m, n), dtype=float)
    for i in range(m):
        for j in range(n):
            dist_matrix[i][j] = np.sum((x1[i]-x2[j])**2)
    return sigma_f**2*np.exp(-0.5/1**2*dist_matrix)

train_X = np.array([1, 3, 7, 9]).reshape(-1, 1)
print(gaussian_kernel(train_X, train_X))