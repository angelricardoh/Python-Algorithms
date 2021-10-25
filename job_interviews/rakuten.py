import random
from random import randint

# Problem 1

# Find 3 numbers such thatn a^3 + b^3 + c^3 = 78

# n = 78
# for i in range(-n, n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if pow(i, 3) + pow(j, 3) + pow(k, 3) == n:
#                 print(str(i) + ' ' + str(j) + ' ' + str(k))

# Problem 3: Using python, write a program that prints out a maze in ASCII. Use # for walls, . for open space, an S for the start of the maze, and an F for the end of the maze
#####
#S.F#
#####

n = 20
maze = []
for i in range(n + 1):
    maze_row = []
    for j in range(n + 1):
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