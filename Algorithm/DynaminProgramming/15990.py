import sys

MOD = 1000000009

T = int(sys.stdin.readline())
n_values = [int(sys.stdin.readline()) for _ in range(T)]

max_n = max(n_values)
dp = [[0] * 4 for _ in range(max_n + 1)]

dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, max_n + 1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

for n in n_values:
    result = sum(dp[n]) % MOD
    sys.stdout.write(str(result) + "\n")
