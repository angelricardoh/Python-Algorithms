import random
from random import randint


n = 20
# maze = [[0] * (n + 1)] * (n + 1)
maze = []
for i in range(n + 1):
    maze_row = []
    for j in range(n + 1):
        # maze[i][j] = '#'
        maze_row.append('#')
    maze.append(maze_row)

for i in range(0, n):
    for j in range(0, 5):
        random_j = randint(0, n)
        maze[i][random_j] = '.'

random_i = randint(0, n)
random_j = randint(0, n)
maze[random_i][random_j] = 'S'


f_random_i = randint(0, n)
f_random_j = randint(0, n)
if f_random_i == random_i and f_random_j == random_j:
    f_random_i = randint(0, n)
    f_random_j = randint(0, n)
maze[f_random_i][f_random_j] = 'F'

print(maze)