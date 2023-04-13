import sys

n = int(sys.stdin.readline().rstrip())

result = 1
for i in range(1, n + 1):
    result *= i
print(result)
