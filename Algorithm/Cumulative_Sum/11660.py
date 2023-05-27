import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

table = [[0] * (n + 1)] * (n + 1)

for i in range(1, n + 1):
    table[i] = [0] + list(map(int, sys.stdin.readline().split()))
    for j in range(1, n + 1):
        table[i][j] += table[i - 1][j] + table[i][j - 1] - table[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    sum = table[x2][y2] - table[x1 - 1][y2] - table[x2][y1 - 1] + table[x1 - 1][y1 - 1]
    print(sum)
