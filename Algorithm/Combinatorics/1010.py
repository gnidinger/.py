import sys
import math

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(math.factorial(m) // (math.factorial(n) * math.factorial(m - n)))
