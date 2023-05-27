import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
w = [0 for _ in range(n + 1)]
v = [0 for _ in range(k + 1)]
memo = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    w[i], v[i] = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if w[i] > j:
            memo[i][j] = memo[i - 1][j]
        else:
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - w[i]] + v[i])

print(memo[n][k])
