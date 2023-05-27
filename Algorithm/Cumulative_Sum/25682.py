import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

lst = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        lst[i][j] = lst[i - 1][j] + lst[i][j - 1] - lst[i - 1][j - 1]
        if (i + j) % 2 == 0 and board[i - 1][j - 1] == 'B':
            lst[i][j] += 1
        elif (i + j) % 2 == 1 and board[i - 1][j - 1] == 'W':
            lst[i][j] += 1

result = n * m

for i in range(k, n + 1):
    for j in range(k, m + 1):
        black = lst[i][j] - lst[i - k][j] - lst[i][j - k] + lst[i - k][j - k]
        white = k**2 - black
        result = min(result, black, white)

print(result)
