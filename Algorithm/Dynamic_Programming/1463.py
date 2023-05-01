import sys

n = int(sys.stdin.readline().rstrip())

memo = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    memo[i] = memo[i - 1] + 1

    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)

    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)

print(memo[n])
