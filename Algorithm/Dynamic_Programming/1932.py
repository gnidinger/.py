import sys

n = int(sys.stdin.readline().rstrip())

lst = [[0 for _ in range(n)] for _ in range(n)]
memo = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    lst[i] = list(map(int, sys.stdin.readline().rstrip().split()))

memo[0][0] = lst[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            memo[i][j] = memo[i - 1][j] + lst[i][j]
        elif j == i:
            memo[i][j] = memo[i - 1][j - 1] + lst[i][j]
        else:
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - 1]) + lst[i][j]

print(max(memo[n - 1]))
