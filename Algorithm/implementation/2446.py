import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    print(" " * i + "*" * (2 * (N - i) - 1))

for i in range(N - 2, -1, -1):
    print(" " * i + "*" * (2 * (N - i) - 1))
