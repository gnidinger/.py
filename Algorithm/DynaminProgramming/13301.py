import sys

n = int(sys.stdin.readline())

if n == 1:
    print(4)
elif n == 2:
    print(6)
else:
    fib = [0] * (n + 1)
    fib[1] = 4
    fib[2] = 6
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    print(fib[n])
