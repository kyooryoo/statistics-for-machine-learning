import pandas as pd
import random

sample_list = []
round_num = 100
person_num = 10

# 这里假设先后有十个玩家参与赌博
for person in range(1, person_num+1):
    money = 10 # 设玩家本金为十元
    # 假设每个玩家最多参加100次赌博
    for round in range(1, round_num+1):
        # 生成或为0或为1的随机数， 模拟抛硬币的过程
        result = random.randint(0, 1)
        # 模拟玩家赌赢或输时本金发生的变化
        if result == 1:
            money = money + 1
        elif result == 0:
            money = money - 1
        # 如果玩家本金输光则推出赌博
        if money == 0:
            break
    sample_list.append([person, round, money])

sample_df = pd.DataFrame(sample_list, columns=['person', 'round', 'money'])
sample_df.set_index('person', inplace=True)
print(sample_df)