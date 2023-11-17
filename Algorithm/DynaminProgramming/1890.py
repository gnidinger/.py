import sys

N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] == 0 or (i == N - 1 and j == N - 1):
            continue
        jump = board[i][j]
        if i + jump < N:
            dp[i + jump][j] += dp[i][j]
        if j + jump < N:
            dp[i][j + jump] += dp[i][j]

print(dp[N - 1][N - 1])
