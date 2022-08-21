from scipy.stats import geom
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 1)
params = [.25, .5]
x = range(1, 11)

for i in range(len(params)):
    geom_rv = geom(p=params[i])
    ax[i].set_title(F"p={params[i]}")
    ax[i].plot(x, geom_rv.pmf(x), 'bo', ms=8)
    ax[i].vlines(x, 0, geom_rv.pmf(x), colors='b', lw=5)
    ax[i].set_xlim(0, 11)
    ax[i].set_ylim(0, .6)
    ax[i].set_xticks(x)
    ax[i].set_yticks([0,.1,.2,.3,.4,.5,.6])
    ax[i].grid(ls='--')

fig.set_tight_layout(True)
plt.show()