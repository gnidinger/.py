import sys

lst = list(map(int, sys.stdin.readline().rstrip().split(" ")))

result = 0

for num in lst:
    result += num**2

print(result % 10)
