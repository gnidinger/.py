import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
memo = [1 for _ in range(n)]
result = 1

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i] and memo[i] < memo[j] + 1:
            memo[i] = memo[j] + 1
            result = max(result, memo[i])

print(result)
