import tkinter as tk
import sys
import numpy as np

UNIT = 40  # pixels
MAZE_H = 5  # grid height
MAZE_W = 5  # grid width


class Maze(tk.Tk, object):
    def __init__(self):
        print("<env init>")
        super(Maze, self).__init__()
        # 动作空间(定义智能体可选的行为),action=0-3
        self.action_space = ['u', 'd', 'l', 'r']
        # 使用变量
        self.n_actions = len(self.action_space)
        self.n_states = 2
        # 配置信息
        self.title('maze')
        self.geometry(f"{int(UNIT*MAZE_H)}x{int(UNIT*MAZE_W)}")
        # 初始化操作
        self.__build_maze()

    def render(self):
        # time.sleep(0.1)
        self.update()

    # def reset(self):
    #     # 智能体回到初始位置
    #     # time.sleep(0.1)
    #     self.update()
    #     self.canvas.delete(self.rect)
    #     # origin = np.array([20, 20])
    #     origin = np.array([20, 20])+np.array([40*np.random.randint(0, 4), 40*np.random.randint(0, 4)])
    #     self.rect = self.canvas.create_rectangle(
    #         origin[0] - 15, origin[1] - 15,
    #         origin[0] + 15, origin[1] + 15,
    #         fill='red')
    #     # return observation
    #     # return (np.array(self.canvas.coords(self.rect)[:2]) - np.array(self.canvas.coords(self.oval)[:2])) / (MAZE_H * UNIT)
    #     return (np.array(self.canvas.coords(self.rect)[:2])) / (MAZE_H * UNIT)
    def reset(self, episode, max_episode):
        # 智能体回到初始位置
        # time.sleep(0.1)
        self.update()
        self.canvas.delete(self.rect)
        # origin = np.array([20, 20])
        origin = np.array([20, 20])+np.array([40*np.random.randint(0, 4), 40*np.random.randint(0, 4)])
        if episode/max_episode > 0.8:
            origin = np.array([20, 20])

        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')
        # return observation
        # return (np.array(self.canvas.coords(self.rect)[:2]) - np.array(self.canvas.coords(self.oval)[:2])) / (MAZE_H * UNIT)
        return (np.array(self.canvas.coords(self.rect)[:2])) / (MAZE_H * UNIT)

    def step(self, action):
        # 智能体向前移动一步：返回next_state,reward,terminal
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:  # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:  # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:  # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:  # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

        next_coords = self.canvas.coords(self.rect)  # next state

        # reward function
        if next_coords == self.canvas.coords(self.oval):
            reward = 1
            print("victory")
            done = True
        elif next_coords in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2), self.canvas.coords(self.hell3), 
                            self.canvas.coords(self.hell4),self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.hell7)]:
            reward = -1
            print("defeat")
            done = True
        else:
            reward = 0
            done = False
        # s_ = (np.array(next_coords[:2]) - np.array(self.canvas.coords(self.oval)[:2])) / (MAZE_H * UNIT)
        s_ = (np.array(next_coords[:2])) / (MAZE_H * UNIT)
        # print(np.array(next_coords[:2]), np.array(self.canvas.coords(self.oval)[:2]), s_)
        return s_, reward, done

    def __build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                                height=MAZE_H * UNIT,
                                width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)
        origin = np.array([20, 20])
        hell1_center = origin + np.array([UNIT * 2, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black')
        ##############
        hell2_center = origin + np.array([UNIT * 2, 0])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black')
        hell3_center = origin + np.array([UNIT * 2, UNIT*4])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 15, hell3_center[1] - 15,
            hell3_center[0] + 15, hell3_center[1] + 15,
            fill='black')
        hell4_center = origin + np.array([UNIT*3, UNIT*3])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 15, hell4_center[1] - 15,
            hell4_center[0] + 15, hell4_center[1] + 15,
            fill='black')
        
        hell5_center = origin + np.array([UNIT*0, UNIT*1])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 15, hell5_center[1] - 15,
            hell5_center[0] + 15, hell5_center[1] + 15,
            fill='black')
        
        hell6_center = origin + np.array([UNIT*1, UNIT*3])
        self.hell6 = self.canvas.create_rectangle(
            hell6_center[0] - 15, hell6_center[1] - 15,
            hell6_center[0] + 15, hell6_center[1] + 15,
            fill='black')
        
        hell7_center = origin + np.array([UNIT*4, UNIT*1])
        self.hell7 = self.canvas.create_rectangle(
            hell7_center[0] - 15, hell7_center[1] - 15,
            hell7_center[0] + 15, hell7_center[1] + 15,
            fill='black')
        
        
        #########
        # oval_center = origin + UNIT * 2
        # self.oval = self.canvas.create_oval(
        #     oval_center[0] - 15, oval_center[1] - 15,
        #     oval_center[0] + 15, oval_center[1] + 15,
        #     fill='yellow')

        # 1
        # oval_center = origin + np.array([3*UNIT, 2*UNIT])
        oval_center = origin + np.array([3*UNIT, 4*UNIT])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')


        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')
        self.canvas.pack()
