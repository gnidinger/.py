import sys

n = int(sys.stdin.readline().rstrip())
wines = [0 for _ in range(n + 1)]
memo = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    wines[i] = int(sys.stdin.readline().rstrip())

memo[1] = wines[1]

if n >= 2:
    memo[2] = memo[1] + wines[2]

for i in range(3, n + 1):
    memo[i] = max(memo[i - 1], memo[i - 2] + wines[i], memo[i - 3] + wines[i - 1] + wines[i])

print(memo[n])
