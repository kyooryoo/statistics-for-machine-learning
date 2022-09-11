import numpy as np
import matplotlib.pyplot as plt

mean = np.array([0, 0]) # 均值为 0
conv = np.array([[1, 0], [0, 1]]) # 方差为 1 协方差为 0

x, y = np.random.multivariate_normal(mean=mean, cov=conv, size=5000).T
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'ro', alpha=0.2)
plt.gca().axes.set_xlim(-4, 4)
plt.gca().axes.set_ylim(-4, 4)
plt.grid(ls='--')
plt.show()