import sys

a = list(map(int, sys.stdin.readline().split()))

a.sort()

if a[0] + a[1] <= a[2]:
    print((a[0] + a[1]) * 2 - 1)
else:
    print(sum(a))
