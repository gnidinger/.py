import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

# if a0 <= n0 * (c - a1) and (a0 / n0 + a1) <= c:

for n in range(n0, 100 + 1):
    if a1 * n + a0 > c * n:
        print(0)
        exit()

print(1)
