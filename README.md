# ReiforceLearning For maze
1. when red block moves to black block, env will be reset and reward -1;
2. only red block move to yellow block, it will be rewarded 1;
3. it is a 4x4 maze looks like frozenlake in gym;
   
![maze](https://github.com/YangQinzhu/ReinforcementLearning/raw/main/figure/maze.png)
![maze_5x5](https://github.com/YangQinzhu/ReinforcementLearning/raw/main/figure/5x5_maze.png)

## DQN
1. In the programe of maze_5x5, it wil chose a random start point in the first 80% episode and it needs to try 20000 episode.

# Result
1. when training episode reach 7000+, it will stop successfully, but it cannot work stably
