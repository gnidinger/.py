import sys

N = int(sys.stdin.readline().rstrip())
dp = [5001] * (N + 1)

dp[0] = 0
if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1

for i in range(6, N + 1):
    if dp[i - 3] != 5001:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if dp[i - 5] != 5001:
        dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[N] if dp[N] != 5001 else -1)
