N, M = map(int, input().split())
# sea = 1, land = 0
map_ = [0 for _ in range(N)]
current = map(int, input().split())
# N = 0, S = 2, E = 1, W = 3
for i in range(M):
    map_[i] = list(map(int, input().split()))

# 이동 좌표 리스트
dx = [(1, 0), (-1, 0)]
dy = [(0, 1), (0, -1)]


