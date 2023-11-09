import sys

MOD = 1000000009

T = int(sys.stdin.readline().rstrip())
test_cases = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

max_n = max(test_cases)
dp = [0] * (max_n + 1)
dp[0] = 1

for i in range(1, max_n + 1):
    if i - 1 >= 0:
        dp[i] += dp[i - 1]
    if i - 2 >= 0:
        dp[i] += dp[i - 2]
    if i - 3 >= 0:
        dp[i] += dp[i - 3]
    dp[i] %= MOD

for n in test_cases:
    print(dp[n])
