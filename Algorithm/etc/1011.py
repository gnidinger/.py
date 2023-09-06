import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    d = y - x

    k = 1
    while k**2 < d:
        k += 1

    if k**2 == d:
        print(2 * k - 1)
    elif k**2 - k < d and d < k**2:
        print(2 * k - 1)
    else:
        print(2 * k - 2)
