import numpy as np
from scipy.stats import uniform
import random

def randomstate_gen(cur_state, transfer_matrix):
    uniform_rvs = uniform().rvs(1)
    i = cur_state-1
    if uniform_rvs[0] <= transfer_matrix[i][0]:
        return 1
    elif uniform_rvs[0] <= transfer_matrix[i][0] + transfer_matrix[i][1]:
        return 2
    else:
        return 3

transfer_matrix = np.array([[.7,.1,.2],[.3,.5,.2],[.1,.3,.6]])
m = 10_000
N = 100_000

cur_state = random.choice([1,2,3])
state_list = []
for i in range(m+N):
    state_list.append(cur_state)
    cur_state = randomstate_gen(cur_state, transfer_matrix)

state_list = state_list[m:]
print(state_list.count(1)/float(len(state_list)))
print(state_list.count(2)/float(len(state_list)))
print(state_list.count(3)/float(len(state_list)))
