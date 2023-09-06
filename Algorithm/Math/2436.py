import sys
import math

g, l = map(int, sys.stdin.readline().rstrip().split())

con = l // g

a = 0
b = 0
mn = sys.maxsize

for i in range(1, int(math.sqrt(con) + 1)):
    if con % i == 0:
        j = con // i
        if math.gcd(i, j) == 1:
            current = i + j
            if current < mn:
                mn = current
                a = i * g
                b = j * g

print(a, b)
