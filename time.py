N = int(input())
time = '000000'
cnt = 0
# 최대 '230000' N = 0 ~ 23
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)