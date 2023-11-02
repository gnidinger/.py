import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [10001] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
