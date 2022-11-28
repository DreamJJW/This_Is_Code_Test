from collections import deque
N, M = map(int, input().split())
maze = []
# 괴물이 있으면 0, 없으면 1
for i in range(N):
    maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:





    



