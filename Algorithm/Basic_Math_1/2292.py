import sys
import math

n = int(sys.stdin.readline())

for i in range(31623):
    sn = 3 * math.pow(i, 2) + 3 * i + 1
    if sn >= n:
        print(i + 1)
        break
