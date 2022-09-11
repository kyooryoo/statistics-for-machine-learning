import numpy as np

mean = np.array([0, 0])
conv = np.array([[1, 0.85], [0.85, 1]])

x_1, y_1 = np.random.multivariate_normal(mean, conv, 3000).T
x_2, y_2 = x_1*100, y_1*100

S_1 = np.vstack((x_1, y_1))
S_2 = np.vstack((x_2, y_2))

print(np.corrcoef(S_1))
print(np.corrcoef(S_2))