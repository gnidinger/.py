import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
result = []

lst = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, n + 1):
    lst[i] = lst[i - 1] + lst[i]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    result.append(lst[end] - lst[start - 1])

print(*result, sep='\n')
