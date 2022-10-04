x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

delta_x = abs(x2 - x1)
delta_y = abs(y2 - y1)

if delta_x == 2 and delta_y == 1:
    print('YES')
elif delta_x == 1 and delta_y == 2:
    print('YES')
else:
    print('NO')

