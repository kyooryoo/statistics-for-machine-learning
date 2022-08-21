import numpy as np
from scipy.stats import binom

# use binom.stats to calculate the mean and var
binom_rv = binom(n=10, p=0.25)
mean, var, skew, kurt=binom_rv.stats(moments='mvsk')
# calculate mean and var from samplings
binom_rvs = binom_rv.rvs(size=100000)
E_sim = np.mean(binom_rvs)
S_sim = np.std(binom_rvs)
V_sim = S_sim * S_sim

print('mean={},var={}'.format(mean,var))
print('E_sim={},V_sim={}'.format(E_sim,V_sim))
# calculate the mean and var from known formula
print('E=np={},V=np(1-p)={}'.format(10 * 0.25,10 * 0.25 * 0.75))