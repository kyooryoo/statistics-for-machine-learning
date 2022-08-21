from scipy.stats import binom
import matplotlib.pyplot as plt

fit, ax = plt.subplots(3, 1, constrained_layout=True)
params = [(10, 0.25), (10, 0.5), (10, 0.8)]
x = range(0, 11)
for i in range(len(params)):
    binom_rv = binom(n=params[i][0], p=params[i][1])
    # take sample 100K times with binom.rvs() function
    rvs = binom_rv.rvs(size=100000)
    # draw the hist graph with the sampling results
    ax[i].hist(rvs, bins=11, density=True, alpha=0.6, edgecolor='k')
    ax[i].set_title('n={}, p={}'.format(params[i][0], params[i][1]))
    ax[i].set_xlim(0, 10)
    ax[i].set_ylim(0, 0.4)
    ax[i].set_xticks(x)
    ax[i].grid(ls='--')
    print('rvs{}:{}'.format(i, rvs))

plt.show()