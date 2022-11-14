N, M = map(int, input().split())
board = [[0] * M for i in range(N)]

for i in range(N):
   board[i] = list(map(int, input()))

def DFS(x, y):
    visited = True
    if board[x][y] == 0:
        board[x][y] = visited
        print(board[x][y], end=' ')
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    DFS(x - 1, y)
    DFS(x + 1, y)
    DFS(x, y + 1)
    DFS(x, y - 1)


res = 0
for i in range(N):
    for j in range(M):
        if DFS(i, j) == True:
            res +=1
print(res)





