import pandas as pd
import random

round_nums = [100, 1_000, 10_000]
person_num = 100_000

# 观察不同轮数情况下的结果
for round_num in round_nums:
    sample_list = []
    for person in range(1, person_num+1):
        money = 10
        for round in range(1, round_num+1):
            result = random.randint(0, 1)
            if result == 1:
                money = money + 1
            elif result == 0:
                money = money - 1
            if money == 0:
                break
        sample_list.append([person, round, money])
    sample_df = pd.DataFrame(sample_list, columns=['person', 'round', 'money'])
    sample_df.set_index('person', inplace=True)
    # 计算没有完成100轮，提前输完了本金推出赌局的玩家数量
    quit_num = person_num-len(sample_df[sample_df['round']==round_num])
    # 计算完成100轮赌局并有盈余的玩家数量
    win_num = len(sample_df[sample_df['money']>10])
    # 计算完成100轮赌局但并没有盈余的玩家数量
    loss_num = len(sample_df[sample_df['round']==round_num]) - win_num

    print(F"总轮数：{round_num}，总人数：{person_num}")
    print(F"输光本金提前出局的人数：{quit_num}")
    print(F"打满全场且盈利的人数：{win_num}")
    print(F"打满全场且亏损的人数：{loss_num}")