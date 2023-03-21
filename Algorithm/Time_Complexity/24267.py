import sys

n = int(sys.stdin.readline())

result = (n * (n - 1) * (n - 2)) // 6

print(result, 3, sep='\n')
