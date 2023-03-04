import sys

n, m = map(int, sys.stdin.readline().split())

list = []

for i in range(n + 1):
    list.append(0)

for i in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for a in range(i, j + 1):
        list[a] = k

print(*list[1:])
