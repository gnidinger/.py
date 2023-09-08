import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split(" ")))
b = list(map(int, sys.stdin.readline().rstrip().split(" ")))

a = sorted(a)
b = sorted(b, reverse=True)

result = 0

for i in range(n):
    result += a[i] * b[i]

print(result)
