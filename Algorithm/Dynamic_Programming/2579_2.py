import sys

n = int(sys.stdin.readline().rstrip())
lst = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(1, n + 1)]
memo = [0 for _ in range(n + 1)]

memo[1] = lst[1]

if n >= 2:
    memo[2] = memo[1] + lst[2]

for i in range(3, n + 1):
    memo[i] = max(memo[i - 2] + lst[i], memo[i - 3] + lst[i - 1] + lst[i])

print(memo[n])
