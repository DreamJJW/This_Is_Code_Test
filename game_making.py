N, M = map(int, input().split())
# sea = 1, land = 0
map_ = [0 for _ in range(N)]
# 현재 좌표 및 방향 입력
current_x, current_y, direction = map(int, input().split())
# N = 0, S = 2, E = 1, W = 3
# 시작 좌표 방문 확인
map_[current_x, current_y] = 1

# 맵 정보 입력받기
for i in range(M):
    map_[i] = list(map(int, input().split()))

# 이동 좌표 리스트
dx = [(1, 0), (-1, 0)]
dy = [(0, 1), (0, -1)]

def TurnLeft():
    global direction
    direction = - 1
    if direction == 0:
        direction = 3

while True:
    if map_[current_x - 1, current_y] == 0:
      TurnLeft()
      current_x =- 1







