import sys

n = int(input())
loss = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [0] * 101

for i in range(n - 1, -1, -1):
    for j in range(100, loss[i], -1):
        dp[j] = max(dp[j], dp[j - loss[i]] + joy[i])

print(max(dp))
