import sys

n, m = map(int, sys.stdin.readline().split())

a = set(sys.stdin.readline().strip().split())
b = set(sys.stdin.readline().strip().split())

# print(len(a.difference(b)) + len(b.difference(a)))
print(len(a ^ b))
