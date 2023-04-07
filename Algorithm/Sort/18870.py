import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().strip().split()))

b = sorted(set(a))

c = {x: i for i, x in enumerate(b)}

for i in a:
    print(c[i], end=' ')

print(c)
