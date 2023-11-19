import sys

n = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
