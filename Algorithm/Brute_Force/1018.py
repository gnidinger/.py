import sys

n, m = map(int, sys.stdin.readline().split())

board = []

for i in range(n):
    board.append(list(sys.stdin.readline().strip()))

cnt = []

for i in range(0, n - 7):
    for j in range(0, m - 7):
        cntw = 0
        cntb = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                coor = a + b - i - j
                if (coor % 2 == 0 and board[a][b] != board[i][j]) or (
                    coor % 2 == 1 and board[a][b] == board[i][j]
                ):
                    cntw += 1
                if (coor % 2 == 0 and board[a][b] == board[i][j]) or (
                    coor % 2 == 1 and board[a][b] != board[i][j]
                ):
                    cntb += 1
        cnt.append(cntw)
        cnt.append(cntb)

print(min(cnt))
