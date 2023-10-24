import sys

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))

dp = lst.copy()

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + lst[i])

print(max(dp))
