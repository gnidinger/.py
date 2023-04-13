import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    c = min(a, b)
    gcd = 1
    for i in range(1, c + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    print(a * b // gcd)
