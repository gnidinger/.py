import sys

n, m = map(int, sys.stdin.readline().split())

list = []

for i in range(n):
    list.append(i + 1)

for i in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    tmp = list[i - 1 : j]
    list[i - 1 : j] = tmp[k - i :] + tmp[: k - i]

print(*list)
