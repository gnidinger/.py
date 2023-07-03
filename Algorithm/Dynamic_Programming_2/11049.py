import sys

n = int(sys.stdin.readline().rstrip())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        k = i + j
        dp[j][k] = float("inf")

        for l in range(j, k):
            cost = dp[j][l] + dp[l + 1][k] + lst[j][0] * lst[l][1] * lst[k][1]
            dp[j][k] = min(dp[j][k], cost)

print(dp[0][n - 1])
