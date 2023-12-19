import sys

r, c, w = map(int, input().split())

dp = [[0] * 31 for _ in range(31)]
dp[1][1] = 1

for i in range(2, 31):
    dp[i][1] = dp[i][i] = 1
    for j in range(2, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

answer = 0
for i in range(r, r + w):
    for j in range(c, c + i - r + 1):
        answer += dp[i][j]

print(answer)
