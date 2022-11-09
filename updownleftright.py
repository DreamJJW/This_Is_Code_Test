N = int(input())
order = list(input().split())
x, y = 1, 1

for i in range(len(order)):
    if order[i] == 'L':
        if y == 1:
            y = 1
        else:
            y = y - 1
    elif order[i] == 'R':
        y = y + 1
    elif order[i] == 'U':
        if x == 1:
            x = 1
        else:
            x = x - 1
    elif order[i] == 'D':
        x = x + 1

print(x, y)


