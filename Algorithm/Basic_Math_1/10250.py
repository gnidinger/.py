import sys
import math

t = int(sys.stdin.readline())

for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    if n <= h:
        a = n
    elif n % h == 0:
        a = h
    else:
        a = n % h
    b = math.ceil(n / h)
    print(100 * a + b)
