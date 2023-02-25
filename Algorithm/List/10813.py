import sys

n, m = map(int, sys.stdin.readline().split())

list = []

for i in range(n + 1):
    list.append(i)

for a in range(m):
    i, j = map(int, sys.stdin.readline().split())
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

print(*list[1:])
