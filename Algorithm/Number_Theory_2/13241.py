import sys

a, b = map(int, sys.stdin.readline().split())
x = max(a, b)
y = min(a, b)

while x % y != 0:
    z = x % y
    x = y
    y = z

print(a * b // y)
