import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
D = int(sys.stdin.readline())

C += D
B += C // 60
C %= 60
A += B // 60
B %= 60
A %= 24

print(A, B, C)
