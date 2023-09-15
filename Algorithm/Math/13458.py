import sys
import math

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

result = 0

for a in A:
    result += 1
    if a > B:
        result += math.ceil((a - B) / C)

print(result)
