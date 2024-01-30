import sys

L = int(sys.stdin.readline().strip())
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())

korean = A // C
math = B // D

if A % C != 0:
    korean += 1

if B % D != 0:
    math += 1

print(L - max(korean, math))
