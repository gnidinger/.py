import sys

n = int(sys.stdin.readline().rstrip())
weight = list(map(int, sys.stdin.readline().rstrip().split(" ")))
m = int(sys.stdin.readline().rstrip())
marble = list(map(int, sys.stdin.readline().rstrip().split(" ")))
dp = [[False for _ in range(40001)] for _ in range(n)]
result = ""

dp[0][0] = True
dp[0][weight[0]] = True

for i in range(1, n):
    for j in range(40001):
        if dp[i - 1][j]:
            dp[i][j] = True
            dp[i][j + weight[i]] = True
            dp[i][abs(j - weight[i])] = True

for i in range(m):
    if marble[i] > 40000 or not dp[n - 1][marble[i]]:
        result += "N "
    else:
        result += "Y "

print(result)
