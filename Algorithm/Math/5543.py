import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())

x = min(a, b, c)
y = min(d, e)

print(x + y - 50)
