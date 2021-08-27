# from maze_env import Maze
from maze_env_hard import Maze
from RL_brain_hard import DQN
import time
import numpy as np

MAX_VICTORY = 10
continue_victory = 0

def run_maze(max_episode):
    print("====Game Start====")
    step = 0
    # max_episode = 100000
    for episode in range(max_episode):
        state = env.reset(episode, max_episode)  # 重置智能体位置
        step_every_episode = 0
        epsilon = episode / max_episode  # 动态变化随机值

        state_set = []
        while True:
            # if episode < 200:
            #     time.sleep(0.1)
            # if episode > max_episode/2:
            #     time.sleep(0.3)
            # if episode > max_episode-200:
            #     time.sleep(0.01)
            env.render()  # 显示新位置
            action = model.choose_action(state, epsilon)  # 根据状态选择行为
            # 环境根据行为给出下一个状态，奖励，是否结束。
            next_state, reward, terminal = env.step(action)
            
            for i in range(len(state_set)):
                if (state_set[i] == next_state).all():
                    reward = -1

            state_set.append(next_state)
            
            model.store_transition(state, action, reward, next_state)  # 模型存储经历
            # 控制学习起始时间(先积累记忆再学习)和控制学习的频率(积累多少步经验学习一次)
            if step > 200 and step % 5 == 0:
                model.learn()
            # 进入下一步
            state = next_state
            if terminal:
                print("episode=", episode, end=",")
                print("step=", step_every_episode)
            
                if reward == 1:
                    continue_victory += 1
                else:
                    continue_victory =0
                if  continue_victory > MAX_VICTORY:
                    print("successfully.")
                    print(max_episode)
                    return
            
            
                break
            step += 1
            step_every_episode += 1
    # 游戏环境结束
    print("====Game Over====")
    env.destroy()


if __name__ == "__main__":
    env = Maze()  # 环境
    print("env.n_states:", env.n_states)
    model = DQN(
        n_states=env.n_states,
        n_actions=env.n_actions
    )  # 算法模型
    run_maze(max_episode=10000*2)
    # run_maze(max_episode=10000)
    env.mainloop()
    model.plot_cost()  # 误差曲线

    # for i in range(1, 110, 10):
    #     max_episode = int(100000*i) #
    #     env = Maze()  # 环境
    #     print("env.n_states:", env.n_states)
    #     model = DQN(
    #         n_states=env.n_states,
    #         n_actions=env.n_actions
    #     )  # 算法模型
    #     run_maze(max_episode)
    #     env.mainloop()
    #     