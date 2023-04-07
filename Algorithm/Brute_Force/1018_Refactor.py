import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

cnt = []
for i in range(n - 7):
    for j in range(m - 7):
        cntw = 0
        cntb = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                coor = a + b - i - j
                if coor % 2 == 0:
                    if board[a][b] != board[i][j]:
                        cntw += 1
                    else:
                        cntb += 1
                else:
                    if board[a][b] == board[i][j]:
                        cntw += 1
                    else:
                        cntb += 1
        cnt.append(cntw)
        cnt.append(cntb)

print(min(cnt))
