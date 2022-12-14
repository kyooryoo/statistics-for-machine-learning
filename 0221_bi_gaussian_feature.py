import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

mean_1 = np.array([0, 0])
mean_2 = np.array([20, -20])
conv = np.array([[34, 12], [12, 41]])
x_1, y_1 = np.random.multivariate_normal(mean_1, conv, 4000).T
x_2, y_2 = np.random.multivariate_normal(mean_2, conv, 4000).T

plt.plot(x_1, y_1, 'ro', alpha=0.05)
plt.plot(x_2, y_2, 'bo', alpha=0.05)
plt.gca().axes.set_xlim(-20, 40)
plt.gca().axes.set_ylim(-40, 20)
evalue, evector = linalg.eig(conv)

print(evalue)
print(evector)
plt.grid(ls='--')
plt.show()