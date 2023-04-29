import sys

n = int(sys.stdin.readline().rstrip())

lst = list(map(int, sys.stdin.readline().rstrip().split()))
memo = [0 for _ in range(n)]

memo[0] = lst[0]
mx = lst[0]

for i in range(1, n):
    memo[i] = max(memo[i - 1] + lst[i], lst[i])
    mx = max(mx, memo[i])

print(mx)
