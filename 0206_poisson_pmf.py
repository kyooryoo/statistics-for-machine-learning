from scipy.stats import poisson
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, 1)
x = range(0, 20)
params = [2, 10, 18]

for i in range(len(params)):
    poisson_rv = poisson(mu=params[i])
    mean, var, skew, kurt = poisson_rv.stats(moments='mvsk')
    ax[i].plot(x, poisson_rv.pmf(x), 'bo', ms=8)
    ax[i].vlines(x, 0, poisson_rv.pmf(x), colors='b', lw=5)
    ax[i].set_title('$\\lambda$={}'.format(params[i]))
    ax[i].set_xticks(x)
    ax[i].set_yticks([0,.1,.2,.3])
    ax[i].grid(ls='--')
    print('lambda={},E[X]={},V[X]={}'.format(params[i], mean, var))

fig.set_tight_layout(True)
plt.show()
    