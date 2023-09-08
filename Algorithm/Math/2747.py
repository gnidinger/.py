import sys

n = int(sys.stdin.readline().rstrip())
memo = [-1 for _ in range(n + 1)]


def fib(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    if memo[x] != -1:
        return memo[x]
    memo[x] = fib(x - 1) + fib(x - 2)
    return memo[x]


print(fib(n))
