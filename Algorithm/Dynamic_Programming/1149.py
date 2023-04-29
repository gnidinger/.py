import sys

n = int(sys.stdin.readline().rstrip())

lst = [[0 for _ in range(n)] for _ in range(n)]
memo = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    lst[i] = list(map(int, sys.stdin.readline().rstrip().split()))

memo[0][0] = lst[0][0]
memo[0][1] = lst[0][1]
memo[0][2] = lst[0][2]

for i in range(1, n):
    memo[i][0] = min(memo[i - 1][1], memo[i - 1][2]) + lst[i][0]
    memo[i][1] = min(memo[i - 1][0], memo[i - 1][2]) + lst[i][1]
    memo[i][2] = min(memo[i - 1][1], memo[i - 1][0]) + lst[i][2]

print(min(memo[n - 1][0], memo[n - 1][1], memo[n - 1][2]))
