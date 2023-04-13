import sys
import math

n = int(sys.stdin.readline())

a = []
b = []

a.append(int(sys.stdin.readline()))

for i in range(1, n):
    x = int(sys.stdin.readline())
    a.append(x)
    b.append(a[i] - a[i - 1])

gcd = b[0]
for i in range(1, len(b)):
    gcd = math.gcd(gcd, b[i])

b = (a[-1] - a[0]) // gcd - len(a[:-1])

print(b)
