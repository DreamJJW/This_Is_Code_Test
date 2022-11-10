n = input()
movesets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]

x_axis = int(ord(n[0])) - 96
y_axis = n[1]
# print(x_axis,y_axis)
cnt = 0

for i in movesets:
    next_x = x_axis + i[0]
    next_y = int(y_axis) + i[1]
    if 9 > next_x > 1 and 9 > next_y > 1:
        cnt += 1

print(cnt)