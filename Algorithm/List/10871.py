import sys

a, b = map(int, sys.stdin.readline().split())

c = list(map(int, sys.stdin.readline().split()))

d = []

for i in range(a):
    if c[i] < b:
        d.append(c[i])

print(*d)