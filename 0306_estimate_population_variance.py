from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

norm_rv = norm(loc=0, scale=1)
x = np.linspace(0, 2, 1000)

sample_n = 100
a_array = []
b_array = []
for i in range(1_000_000):
    norm_rvs = norm_rv.rvs(size=sample_n)
    x_bar = sum(norm_rvs) / float(sample_n)
    a = sum(np.square((norm_rvs - x_bar))) / float(sample_n)
    b = sum(np.square((norm_rvs - x_bar))) / float(sample_n-1)
    a_array.append(a)
    b_array.append(b)

print(np.mean(a_array))
print(np.mean(b_array))
plt.hist(a_array, bins=100, density=True, alpha=0.3, edgecolor='k', label="n")
plt.hist(b_array, bins=100, density=True, alpha=0.3, edgecolor='m', label="n-1")
plt.axvline(1, ymax=0.8, color='r')
plt.gca().axes.set_xlim(0.4, 1.6)
plt.legend(loc='best')
plt.grid(ls='--')
plt.show()