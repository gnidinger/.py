import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

dp = [[0] * (N + 1) for _ in range(K + 1)]
mod = 1000000000

for i in range(N + 1):
    dp[1][i] = 1


for k in range(2, K + 1):
    for n in range(N + 1):
        for m in range(n + 1):
            dp[k][n] += dp[k - 1][n - m]
            dp[k][n] %= mod

print(dp[K][N])
