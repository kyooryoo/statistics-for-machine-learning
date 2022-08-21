import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, 1)
x = range(0, 20)
params = [2, 10, 18]

for i in range(len(params)):
    lambda_ = params[i]
    data = poisson.rvs(mu=lambda_, size=100000)
    ax[i].hist(data, density=True, alpha=0.6, edgecolor='k')
    ax[i].set_title('$\\lambda$={}'.format(params[i]))
    print('mean=', np.mean(data))
    print('var=', np.square(np.std(data)))
    ax[i].grid(ls='--')

fig.set_tight_layout(True)
plt.show()