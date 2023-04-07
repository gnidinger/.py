import sys

n, m = map(int, sys.stdin.readline().strip().split())

a = dict()
b = dict()

for i in range(n):
    x = sys.stdin.readline().strip()
    a[i + 1] = x
    b[x] = i + 1

for _ in range(m):
    x = sys.stdin.readline().strip()
    if x.isdigit():
        print(a[int(x)])
    else:
        print(b[x])
