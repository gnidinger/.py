import sys

n = int(sys.stdin.readline())

if n == 0:
    sys.stdout.write("0\n")
elif n == 1:
    sys.stdout.write("1\n")
else:
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    sys.stdout.write(str(fib[n]) + "\n")
