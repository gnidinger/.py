import sys

t = int(sys.stdin.readline())


def result(k, n):
    if k == 0:
        return n
    if n == 1:
        return 1
    return result(k - 1, n) + result(k, n - 1)


for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(result(k, n))
