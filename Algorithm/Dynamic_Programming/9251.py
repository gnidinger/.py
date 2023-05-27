import sys

n = sys.stdin.readline().rstrip()
m = sys.stdin.readline().rstrip()

ln = len(n)
lm = len(m)

memo = [[0 for _ in range(lm + 1)] for _ in range(ln + 1)]

for i in range(1, ln + 1):
    for j in range(1, lm + 1):
        if n[i - 1] == m[j - 1]:
            memo[i][j] = memo[i - 1][j - 1] + 1
        else:
            memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

print(memo[ln][lm])
