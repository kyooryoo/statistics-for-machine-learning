import numpy as np
import matplotlib.pyplot as plt

# 状态转移矩阵
transfer_matrix = np.array([[.7,.1,.2],[.3,.5,.2],[.1,.3,.6]])
# 准备三个初始状态矢量
start_state_array = ([[.5,.3,.2],[.13,.28,.59],[.1,.85,.05]])

trans_step = 10

for i in range(3):
    state_1_value = []
    state_2_value = []
    state_3_value = []
    for _ in range(trans_step):
        start_state_array[i] = np.dot(start_state_array[i], transfer_matrix)
        state_1_value.append(start_state_array[i][0])
        state_2_value.append(start_state_array[i][1])
        state_3_value.append(start_state_array[i][2])
    
    x = np.arange(trans_step)
    plt.plot(x, state_1_value, label='state_1', marker='o')
    plt.plot(x, state_2_value, label='state_2', marker='s')
    plt.plot(x, state_3_value, label='state_3', marker='v')
    plt.legend()
    print(start_state_array[i])

plt.gca().axes.set_xticks(np.arange(0, trans_step))
plt.gca().axes.set_yticks(np.arange(.2,.6,.05))
plt.gca().axes.set_xlabel('n step')
plt.gca().axes.set_ylabel('p')
plt.grid(ls='--')
plt.show()
