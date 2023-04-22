import sys

n = int(sys.stdin.readline().rstrip())

result = [[' '] * n for _ in range(n)]


def star(n, x, y):
    if n == 1:
        result[y][x] = '*'
        return

    m = n // 3
    for dy in range(3):
        for dx in range(3):
            if dx == 1 and dy == 1:
                continue
            star(m, x + m * dx, y + m * dy)


star(n, 0, 0)

for i in result:
    print(''.join(i))
