N, M = map(int , input().split())
max_num = 0
for i in range(N):
    card = list(map(int, input().split()))
    min_num = min(card)
    if min_num > max_num:
        max_num = min_num
print(max_num)