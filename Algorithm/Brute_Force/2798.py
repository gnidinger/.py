import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
int_list = list(map(int, sys.stdin.readline().split()))
result = m

for i in combinations(int_list, 3):
    temp = sum(i)
    if temp > m:
        continue
    result = min(result, m - temp)

print(m - result)
