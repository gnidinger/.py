import sys

a, b = sys.stdin.readline().strip().split()

A = list(a)
B = list(b)
A.reverse()
B.reverse()

a = int(''.join(A))
b = int(''.join(B))

print(max(a, b))
